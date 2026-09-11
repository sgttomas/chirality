#include <errno.h>
#include <limits.h>
#include <signal.h>
#include <spawn.h>
#include <stdbool.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <time.h>
#include <unistd.h>

#if !defined(__APPLE__) || !defined(POSIX_SPAWN_CLOEXEC_DEFAULT)
#error "The native probe watchdog requires the reviewed macOS spawn boundary"
#endif

extern char **environ;

enum {
  EXIT_WATCHDOG_TIMEOUT = 124,
  EXIT_WATCHDOG_CLEANUP = 125,
  FIXTURE_MAX_LIFETIME_SECONDS = 12,
  MINIMUM_FIXTURE_FALLBACK_SECONDS = FIXTURE_MAX_LIFETIME_SECONDS + 2,
};

static volatile sig_atomic_t interrupted_signal = 0;
static int monotonic_error = 0;
static void interrupt_handler(int signal_number) { interrupted_signal = signal_number; }

static int64_t monotonic_milliseconds(void) {
  struct timespec value;
  if (clock_gettime(CLOCK_MONOTONIC, &value) != 0) {
    int captured_errno = errno;
    if (monotonic_error == 0) monotonic_error = captured_errno;
    return -1;
  }
  return (int64_t)value.tv_sec * 1000 + value.tv_nsec / 1000000;
}

static bool sleep_until_or_for(int64_t deadline, int milliseconds, bool interruptible) {
  int64_t now = monotonic_milliseconds();
  if (now < 0 || now >= deadline) return false;
  int64_t remaining = deadline - now;
  if (remaining < milliseconds) milliseconds = (int)remaining;
  struct timespec delay = {milliseconds / 1000, (milliseconds % 1000) * 1000000L};
  while (nanosleep(&delay, &delay) != 0 && errno == EINTR) {
    if (interruptible && interrupted_signal != 0) return false;
  }
  return monotonic_milliseconds() < deadline;
}

static bool parse_seconds(const char *value, int minimum, int maximum, int *result) {
  char *end = NULL;
  errno = 0;
  long parsed = strtol(value, &end, 10);
  if (errno != 0 || end == value || *end != '\0' || parsed < minimum || parsed > maximum) return false;
  *result = (int)parsed;
  return true;
}

static bool canonical_executable(const char *value) {
  char resolved[PATH_MAX];
  struct stat link_metadata, metadata;
  return value[0] == '/' && lstat(value, &link_metadata) == 0 && !S_ISLNK(link_metadata.st_mode)
    && realpath(value, resolved) != NULL && strcmp(value, resolved) == 0
    && stat(value, &metadata) == 0 && S_ISREG(metadata.st_mode) && access(value, X_OK) == 0;
}

static bool canonical_directory(const char *value) {
  char resolved[PATH_MAX];
  struct stat link_metadata, metadata;
  return value[0] == '/' && lstat(value, &link_metadata) == 0 && !S_ISLNK(link_metadata.st_mode)
    && realpath(value, resolved) != NULL && strcmp(value, resolved) == 0
    && stat(value, &metadata) == 0 && S_ISDIR(metadata.st_mode);
}

static bool exact_closed_environment(void) {
  const char *names[] = {"ELECTRON_RUN_AS_NODE=", "HOME=", "LANG=", "PATH=", "TMPDIR="};
  bool seen[] = {false, false, false, false, false};
  size_t count = 0;
  for (; environ[count] != NULL; count++) {
    bool matched = false;
    for (size_t index = 0; index < 5; index++) {
      size_t prefix = strlen(names[index]);
      if (strncmp(environ[count], names[index], prefix) != 0 || seen[index]) continue;
      const char *value = environ[count] + prefix;
      if ((index == 0 && strcmp(value, "1") != 0)
        || (index == 1 && !canonical_directory(value))
        || (index == 2 && strcmp(value, "en_US.UTF-8") != 0)
        || (index == 3 && strcmp(value, "/usr/bin:/bin:/usr/sbin:/sbin") != 0)
        || (index == 4 && !canonical_directory(value))) return false;
      seen[index] = true;
      matched = true;
      break;
    }
    if (!matched) return false;
  }
  return count == 5 && seen[0] && seen[1] && seen[2] && seen[3] && seen[4];
}

static int observe_leader(pid_t pid, siginfo_t *result, int *error_number) {
  memset(result, 0, sizeof(*result));
  int status;
  do { status = waitid(P_PID, (id_t)pid, result, WEXITED | WNOHANG | WNOWAIT); }
  while (status != 0 && errno == EINTR && interrupted_signal == 0);
  int captured_errno = status == 0 ? 0 : errno;
  *error_number = captured_errno;
  if (status != 0) return -1;
  return result->si_pid == pid ? 1 : 0;
}

static int wait_for_leader(pid_t pid, int64_t deadline, siginfo_t *result, bool interruptible, int *error_number) {
  for (;;) {
    int observed = observe_leader(pid, result, error_number);
    if (observed != 0) return observed;
    if ((interruptible && interrupted_signal != 0) || !sleep_until_or_for(deadline, 20, interruptible)) return 0;
  }
}

static bool signal_anchored_group(pid_t pid, int signal_number, int *signal_result, int *error_number) {
  int result = kill(-pid, signal_number);
  int captured_errno = result == 0 ? 0 : errno;
  *signal_result = result;
  *error_number = captured_errno;
  return result == 0 || captured_errno == ESRCH;
}

static bool reap_observed_leader(pid_t pid, int *status, pid_t *reap_result, int *error_number) {
  pid_t result;
  do { result = waitpid(pid, status, 0); } while (result < 0 && errno == EINTR);
  int captured_errno = result < 0 ? errno : 0;
  *reap_result = result;
  *error_number = captured_errno;
  return result == pid;
}

static bool group_retired_after_reap(pid_t pid, int64_t deadline, int *probe_result, int *error_number, bool *deadline_expired) {
  for (;;) {
    errno = 0;
    int result = kill(-pid, 0);
    int captured_errno = result == 0 ? 0 : errno;
    *probe_result = result;
    *error_number = captured_errno;
    if (result < 0 && captured_errno == ESRCH) return true;
    if (!sleep_until_or_for(deadline, 20, false)) {
      *deadline_expired = true;
      return false;
    }
  }
}

static void print_diagnostics(pid_t child, bool timed_out, int initial_observation, int initial_waitid_errno,
  bool term_attempted, int grace_observation, int grace_waitid_errno, bool kill_wait_attempted,
  int kill_observation, int kill_waitid_errno,
  int term_result, int term_errno, int kill_result, int kill_errno, pid_t reap_result,
  bool reap_attempted, int reap_status, int reap_errno, bool group_probe_attempted,
  int group_probe_result, int group_probe_errno,
  bool group_absent, bool group_deadline_expired, bool fallback_required, bool fallback_elapsed) {
  fprintf(stderr,
    "chirality-watchdog:diagnostic {\"childPid\":%d,\"timedOut\":%s,"
    "\"initialObservation\":%d,\"initialWaitidErrno\":%d,"
    "\"termAttempted\":%s,\"graceObservation\":%d,\"graceWaitidErrno\":%d,"
    "\"killWaitAttempted\":%s,\"killObservation\":%d,\"killWaitidErrno\":%d,"
    "\"termResult\":%d,\"termErrno\":%d,\"killResult\":%d,\"killErrno\":%d,"
    "\"reapAttempted\":%s,\"reapResult\":%d,\"reapStatus\":%d,\"reapErrno\":%d,"
    "\"groupProbeAttempted\":%s,\"groupProbeResult\":%d,\"groupProbeErrno\":%d,\"groupAbsent\":%s,"
    "\"groupDeadlineExpired\":%s,\"monotonicErrno\":%d,"
    "\"fallbackRequired\":%s,\"fallbackElapsed\":%s}\n",
    child, timed_out ? "true" : "false", initial_observation, initial_waitid_errno,
    term_attempted ? "true" : "false", grace_observation, grace_waitid_errno,
    kill_wait_attempted ? "true" : "false", kill_observation, kill_waitid_errno,
    term_result, term_errno, kill_result, kill_errno, reap_attempted ? "true" : "false",
    reap_result, reap_status, reap_errno, group_probe_attempted ? "true" : "false",
    group_probe_result, group_probe_errno, group_absent ? "true" : "false",
    group_deadline_expired ? "true" : "false", monotonic_error,
    fallback_required ? "true" : "false", fallback_elapsed ? "true" : "false");
}

static bool bounded_fallback_wait(int seconds) {
  if (seconds == 0) return true;
  int64_t started = monotonic_milliseconds();
  if (started < 0) return false;
  int64_t deadline = started + (int64_t)seconds * 1000;
  for (;;) {
    int64_t now = monotonic_milliseconds();
    if (now < 0) return false;
    if (now >= deadline) return true;
    int64_t remaining = deadline - now;
    struct timespec delay = {0, (remaining < 50 ? remaining : 50) * 1000000L};
    while (nanosleep(&delay, &delay) != 0) {
      if (errno != EINTR) return false;
    }
  }
}

static int child_exit_code(int status) {
  if (WIFEXITED(status)) return WEXITSTATUS(status);
  if (WIFSIGNALED(status)) {
    int result = 128 + WTERMSIG(status);
    return result > 255 ? 255 : result;
  }
  return EXIT_WATCHDOG_CLEANUP;
}

int main(int argc, char **argv) {
  if (argc < 9 || strcmp(argv[1], "--timeout-seconds") != 0
    || strcmp(argv[3], "--term-grace-seconds") != 0
    || strcmp(argv[5], "--fixture-fallback-seconds") != 0
    || strcmp(argv[7], "--") != 0) {
    fputs("chirality-watchdog:invalid-arguments\n", stderr);
    return EXIT_WATCHDOG_CLEANUP;
  }
  int timeout_seconds, grace_seconds, fixture_fallback_seconds;
  if (!parse_seconds(argv[2], 1, 300, &timeout_seconds)
    || !parse_seconds(argv[4], 1, 30, &grace_seconds)
    || !parse_seconds(argv[6], 0, 300, &fixture_fallback_seconds)
    || (fixture_fallback_seconds != 0 && fixture_fallback_seconds < MINIMUM_FIXTURE_FALLBACK_SECONDS)
    || !canonical_executable(argv[8]) || !exact_closed_environment()) {
    fputs("chirality-watchdog:invalid-boundary\n", stderr);
    return EXIT_WATCHDOG_CLEANUP;
  }

  struct sigaction action = {0};
  action.sa_handler = interrupt_handler;
  sigemptyset(&action.sa_mask);
  if (sigaction(SIGINT, &action, NULL) != 0 || sigaction(SIGTERM, &action, NULL) != 0 || sigaction(SIGHUP, &action, NULL) != 0) {
    fputs("chirality-watchdog:signal-handler-unavailable\n", stderr);
    return EXIT_WATCHDOG_CLEANUP;
  }

  posix_spawn_file_actions_t actions;
  if (posix_spawn_file_actions_init(&actions) != 0) return EXIT_WATCHDOG_CLEANUP;
  int error = posix_spawn_file_actions_addinherit_np(&actions, STDIN_FILENO);
  if (error == 0) error = posix_spawn_file_actions_addinherit_np(&actions, STDOUT_FILENO);
  if (error == 0) error = posix_spawn_file_actions_addinherit_np(&actions, STDERR_FILENO);
  posix_spawnattr_t attributes;
  bool attributes_initialized = false;
  if (error == 0) {
    error = posix_spawnattr_init(&attributes);
    attributes_initialized = error == 0;
  }
  short flags = POSIX_SPAWN_CLOEXEC_DEFAULT | POSIX_SPAWN_SETPGROUP;
  if (error == 0) error = posix_spawnattr_setflags(&attributes, flags);
  if (error == 0) error = posix_spawnattr_setpgroup(&attributes, 0);
  pid_t child = -1;
  if (error == 0) error = posix_spawn(&child, argv[8], &actions, &attributes, &argv[8], environ);
  if (attributes_initialized) posix_spawnattr_destroy(&attributes);
  posix_spawn_file_actions_destroy(&actions);
  if (error != 0 || child <= 0) {
    fputs("chirality-watchdog:spawn-failed\n", stderr);
    return EXIT_WATCHDOG_CLEANUP;
  }

  bool timed_out = false;
  bool cleanup_failed = false;
  bool signal_failed = false;
  siginfo_t observed;
  int initial_waitid_errno = 0, grace_waitid_errno = 0, kill_waitid_errno = 0;
  int term_result = 0, term_errno = 0, kill_result = 0, kill_errno = 0;
  pid_t reap_result = 0;
  int reap_errno = 0, group_probe_result = 0, group_probe_errno = 0;
  bool group_absent = false, group_deadline_expired = false;
  int64_t deadline = monotonic_milliseconds() + (int64_t)timeout_seconds * 1000;
  int initial_observation = wait_for_leader(child, deadline, &observed, true, &initial_waitid_errno);
  int grace_observation = 0, kill_observation = 0;
  bool term_attempted = false, kill_wait_attempted = false;
  int observation = initial_observation;
  if (observation <= 0) {
    timed_out = true;
    term_attempted = true;
    if (!signal_anchored_group(child, SIGTERM, &term_result, &term_errno)) signal_failed = true;
    int64_t grace_deadline = monotonic_milliseconds() + (int64_t)grace_seconds * 1000;
    grace_observation = wait_for_leader(child, grace_deadline, &observed, false, &grace_waitid_errno);
    observation = grace_observation;
  }

  // The leader remains unreaped here and anchors its process-group identity.
  // KILL always precedes reap, including after a normal leader exit, so an
  // unexpected live Electron descendant cannot outlive a successful probe.
  if (!signal_anchored_group(child, SIGKILL, &kill_result, &kill_errno)) signal_failed = true;
  if (observation <= 0) {
    kill_wait_attempted = true;
    int64_t kill_deadline = monotonic_milliseconds() + 5000;
    kill_observation = wait_for_leader(child, kill_deadline, &observed, false, &kill_waitid_errno);
    observation = kill_observation;
  }

  int status = 0;
  bool reap_attempted = observation == 1;
  bool leader_reaped = reap_attempted
    && reap_observed_leader(child, &status, &reap_result, &reap_errno);
  if (!leader_reaped) cleanup_failed = true;
  // PID/PGID can be reused after reap. This branch only diagnoses absence and
  // never sends another signal. A signal error alone cannot skip this proof:
  // XNU may return EPERM when group iteration finds only a zombie leader.
  bool group_probe_attempted = leader_reaped;
  if (group_probe_attempted) {
    int64_t group_deadline = monotonic_milliseconds() + 2000;
    group_absent = group_retired_after_reap(child, group_deadline, &group_probe_result,
      &group_probe_errno, &group_deadline_expired);
    if (!group_absent) cleanup_failed = true;
  }

  // Signal errors remain in the structured diagnostic. Once the exact leader
  // is reaped, however, confirmed group absence is the terminal cleanup proof.
  // Observation/reap/group/clock/fallback failures remain independently fatal.
  if (signal_failed && !(leader_reaped && group_absent)) cleanup_failed = true;

  int exit_code = cleanup_failed ? EXIT_WATCHDOG_CLEANUP : child_exit_code(status);
  bool fallback_required = fixture_fallback_seconds != 0;
  bool fallback_elapsed = bounded_fallback_wait(fixture_fallback_seconds);
  if (!fallback_elapsed) cleanup_failed = true;
  if (monotonic_error != 0) cleanup_failed = true;
  print_diagnostics(child, timed_out, initial_observation, initial_waitid_errno,
    term_attempted, grace_observation, grace_waitid_errno, kill_wait_attempted,
    kill_observation, kill_waitid_errno,
    term_result, term_errno, kill_result, kill_errno, reap_result, reap_attempted,
    status, reap_errno, group_probe_attempted, group_probe_result, group_probe_errno,
    group_absent, group_deadline_expired,
    fallback_required, fallback_elapsed);
  if (cleanup_failed) {
    fprintf(stderr, "chirality-watchdog:cleanup-unverified timeout=%s fallbackElapsed=%s\n",
      timed_out ? "true" : "false", fallback_required && fallback_elapsed ? "true" : "false");
    return EXIT_WATCHDOG_CLEANUP;
  }
  if (timed_out) {
    fprintf(stderr, "chirality-watchdog:deadline-exceeded fallbackElapsed=%s\n", fixture_fallback_seconds != 0 ? "true" : "false");
    return EXIT_WATCHDOG_TIMEOUT;
  }
  fprintf(stderr, "chirality-watchdog:child-retired exit=%d fallbackElapsed=%s\n", exit_code, fallback_required && fallback_elapsed ? "true" : "false");
  return exit_code;
}
