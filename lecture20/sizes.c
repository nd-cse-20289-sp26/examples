/* sizes.c: sizes of types */

#include <stdbool.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
    printf("sizeof(char)   = %lu\n", sizeof(char));
    printf("sizeof(int)    = %lu\n", sizeof(int));
    printf("sizeof(double) = %lu\n", sizeof(double));
    printf("sizeof(void *) = %lu\n", sizeof(void *));
    return EXIT_SUCCESS;
}
