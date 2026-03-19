/* dump_bits.c */

#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

/* Macros */

#define DUMP_BITS(_v) \
    for (int _i = sizeof(_v)*8 - 1; _i >= 0; _i--) {\
        if ((_i + 1) % 8 == 0) putc(' ', stdout); \
        putc(((_v) & 1<<_i) ? '1' : '0', stdout); \
    } \
    putc('\n', stdout);

/* Main Execution */

int main(int argc, char *argv[]) {
    /* Signed and Unsigned are the same underlying bits */
    int         i = 0xDEADBEEF;
    unsigned    u = 0xDEADBEEF;

    DUMP_BITS(i);
    DUMP_BITS(u);
    printf("i = %d, u = %u, i == u ? %d\n", i, u, i == u);  // Formatting

    /* Need to be careful with overflowing integer range */
#if 0
    for (int8_t b = 0; b < (1<<8); b++) {   // Overflows into infinite loop
    	DUMP_BITS(b);
    }

    for (int c = 0; c < (1<<8); c++) {      // Fix by using larger int
        int8_t b = c;
    	DUMP_BITS(b);
    }
#endif

    /* Intel machines are little endian. */
#if 0
    int8_t *a = (int8_t *)&u;               // Cast into array
    for (int i = sizeof(u) - 1; i >= 0; i--) {
        printf("%lx = %hhx\n", (intptr_t)&a[i], a[i]);
    }
#endif

    return EXIT_SUCCESS;
}

/* vim: set sts=4 sw=4 ts=8 expandtab ft=c: */
