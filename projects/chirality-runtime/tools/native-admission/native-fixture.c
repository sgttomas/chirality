#include <errno.h>
#include <fcntl.h>
#include <libproc.h>
#include <signal.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/types.h>
#include <unistd.h>

extern char **environ;

enum { FIXTURE_MAX_LIFETIME_SECONDS = 12, DESCENDANT_MAX_LIFETIME_SECONDS = 4 };

static void fixture_timeout(int signal_number) {
  (void)signal_number;
  _exit(124);
}

static void hex(const unsigned char *bytes, size_t length) {
  static const char digits[] = "0123456789abcdef";
  for (size_t i = 0; i < length; i++) {
    putchar(digits[bytes[i] >> 4]);
    putchar(digits[bytes[i] & 15]);
  }
}

static void string_hex(const char *value) { hex((const unsigned char *)value, strlen(value)); }

static void emit_role(const char *event, pid_t child) {
  printf("{\"event\":\"%s\",\"pid\":%d,\"pgrp\":%d,\"childPid\":%d}\n",
         event, getpid(), getpgrp(), child);
}

static int inspect(void) {
  unsigned char bootstrap[65];
  size_t length = 0;
  for (;;) {
    ssize_t count = read(3, bootstrap + length, sizeof(bootstrap) - length);
    if (count < 0 && errno == EINTR) continue;
    if (count < 0) return 20;
    if (count == 0) break;
    length += (size_t)count;
    if (length == sizeof(bootstrap)) return 21;
  }
  char cwd[4096];
  if (!getcwd(cwd, sizeof(cwd))) return 22;
  int capacity = 256;
  struct proc_fdinfo *fds = NULL;
  int bytes = 0;
  for (;;) {
    if (capacity > 1048576) return 23;
    free(fds);
    fds = calloc((size_t)capacity, sizeof(*fds));
    if (!fds) return 24;
    bytes = proc_pidinfo(getpid(), PROC_PIDLISTFDS, 0, fds, capacity * (int)sizeof(*fds));
    if (bytes <= 0) { free(fds); return 25; }
    if (bytes < capacity * (int)sizeof(*fds)) break;
    capacity *= 2;
  }
  int fd_count = bytes / (int)sizeof(*fds);
  printf("{\"event\":\"inspect\",\"pid\":%d,\"pgrp\":%d,\"cwdHex\":\"", getpid(), getpgrp());
  string_hex(cwd);
  printf("\",\"bootstrapHex\":\"");
  hex(bootstrap, length);
  printf("\",\"bootstrapLength\":%zu,\"fdEnumeration\":\"PROC_PIDLISTFDS\",\"openFds\":[", length);
  for (int index = 0; index < fd_count; index++) printf("%s%d", index ? "," : "", fds[index].proc_fd);
  free(fds);
  size_t environment_count = 0;
  while (environ[environment_count]) environment_count++;
  printf("],\"environmentCount\":%zu,\"environmentHex\":[", environment_count);
  for (size_t index = 0; index < environment_count; index++) {
    printf("%s\"", index ? "," : "");
    string_hex(environ[index]);
    putchar('"');
  }
  printf("]}\n");
  return 0;
}

static void child_term(int signal_number) {
  (void)signal_number;
  static const char message[] = "{\"event\":\"descendant-term-survived\"}\n";
  (void)write(STDOUT_FILENO, message, sizeof(message) - 1);
}

static void child_alarm(int signal_number) {
  (void)signal_number;
  static const char message[] = "{\"event\":\"descendant-self-exit\"}\n";
  (void)write(STDOUT_FILENO, message, sizeof(message) - 1);
  _exit(0);
}

static int descendant(void) {
  pid_t child = fork();
  if (child < 0) return 30;
  if (child == 0) {
    struct sigaction term = {0}, alarm_action = {0};
    term.sa_handler = child_term;
    alarm_action.sa_handler = child_alarm;
    sigemptyset(&term.sa_mask);
    sigemptyset(&alarm_action.sa_mask);
    if (sigaction(SIGTERM, &term, NULL) || sigaction(SIGALRM, &alarm_action, NULL)) _exit(31);
    // Interval timers are not inherited across fork. Bind the descendant's
    // lifetime explicitly even if its Electron probe host disappears.
    alarm(DESCENDANT_MAX_LIFETIME_SECONDS);
    emit_role("descendant-ready", 0);
    for (;;) pause();
  }
  emit_role("leader-ready", child);
  for (;;) pause();
}

int main(int argc, char **argv) {
  setvbuf(stdout, NULL, _IONBF, 0);
  struct sigaction lifetime = {0};
  lifetime.sa_handler = fixture_timeout;
  sigemptyset(&lifetime.sa_mask);
  if (sigaction(SIGALRM, &lifetime, NULL) != 0) return 3;
  // Every fixture mode is bounded independently of the JavaScript host.
  alarm(FIXTURE_MAX_LIFETIME_SECONDS);
  if (argc < 2) return 2;
  if (!strcmp(argv[1], "inspect") && argc == 2) return inspect();
  if (!strcmp(argv[1], "echo") && argc == 2) {
    unsigned char bytes[4096];
    for (;;) {
      ssize_t count = read(STDIN_FILENO, bytes, sizeof(bytes));
      if (count < 0 && errno == EINTR) continue;
      if (count < 0) return 40;
      if (count == 0) return 0;
      size_t offset = 0;
      while (offset < (size_t)count) {
        ssize_t written = write(STDOUT_FILENO, bytes + offset, (size_t)count - offset);
        if (written < 0 && errno == EINTR) continue;
        if (written <= 0) return 41;
        offset += (size_t)written;
      }
    }
  }
  if (!strcmp(argv[1], "exit") && argc == 3) {
    char *end = NULL;
    long value = strtol(argv[2], &end, 10);
    if (!end || *end || value < 0 || value > 125) return 2;
    return (int)value;
  }
  if (!strcmp(argv[1], "hold") && argc == 2) {
    emit_role("leader-ready", 0);
    for (;;) pause();
  }
  if (!strcmp(argv[1], "descendant") && argc == 2) return descendant();
  return 2;
}
