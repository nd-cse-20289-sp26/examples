/* intbytes.c */

#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <arpa/inet.h>

/* Data Union */

union Data {
    int32_t number;
    uint8_t bytes[sizeof(int32_t)];
    uint8_t letter;
};

/* Main Execution */

int main(int argc, char *argv[]) {
    union Data data;	// We can shorten this w/ type definition

    printf("sizeof(data) = %ld bytes\n", sizeof(data));

    for (int i = 1; i < argc; i++) {
	data.number = strtol(argv[i], NULL, 10);

	for (int c = 0; c < sizeof(int32_t); c++) {
	    printf("%d: %02x (%3d)\n", c, data.bytes[c], data.bytes[c]);
	}
	printf("%d, %s, %c\n", data.number, data.bytes, data.letter);
	putchar('\n');
    }

    return EXIT_SUCCESS;
}

/* vim: set sts=4 sw=4 ts=8 expandtab ft=c: */
