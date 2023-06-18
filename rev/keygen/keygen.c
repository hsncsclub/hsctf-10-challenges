#include <stdio.h>
#include <string.h>

const char* const s = "lfkmq<8=?=>?l'==<2'<;=>'?l<i'<l<9<h9l::::w";
int main(int argc, char** argv) {
	if (argc != 2 || strlen(argv[1]) != strlen(s)) {
		puts("Wrong");
		return 1;
	}
	for (const char *c = argv[1], *d = s; *c != 0; c++, d++) {
		if ((*c ^ 10) != *d) {
			puts("Wrong");
			return 1;
		}
	}
	puts("Correct");
}