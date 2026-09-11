#include <errno.h>
#include <signal.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

extern char **environ;

int main(int argc, char **argv) {
  if (argc < 4) {
    fputs("usage: p2-host-xpc-expiring-exec SECONDS EXECUTABLE ARG...\n", stderr);
    return 64;
  }
  char *end = NULL;
  long seconds = strtol(argv[1], &end, 10);
  if (!end || *end != '\0' || seconds < 1 || seconds > 120 || argv[2][0] != '/') {
    fputs("invalid expiring-exec input\n", stderr);
    return 64;
  }
  if (signal(SIGALRM, SIG_DFL) == SIG_ERR || alarm((unsigned int)seconds) != 0) {
    perror("alarm");
    return 70;
  }
  execve(argv[2], &argv[2], environ);
  int saved = errno;
  errno = saved;
  perror("execve");
  return 71;
}
