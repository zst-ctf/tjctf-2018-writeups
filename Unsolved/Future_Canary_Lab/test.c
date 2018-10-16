#include <stdio.h>
#include <stdlib.h>

#define FLAG "-----REDACTED-----"

void interview(int secret) {

    int i, j;
    int canary[10];
    char name[64];
    int check[10];

    for (i = 0; i < 10; ++i) {
        canary[i] = check[i] = rand();
    }

    printf("Welcome to the Future Canary Lab!\n");
    printf("What is your name?\n");
    gets(name);

    for (int x = 0; x < 10; ++x) {
        printf(">> check[%d] %x\n", x, check[x]);
    }

    for (j = 0; j < 10; ++j) {
        printf(">> canary %x = check %x\n", canary[j], check[j]);
        if (canary[j] != check[j]) {
            printf("Alas, it would appear you lack the time travel powers we desire.\n");
            exit(0);
        }
    }

    printf(">> Secret 0x%x\n", secret);
    printf(">> i 0x%x\n", i);
    printf(">> j 0x%x\n", j);
    printf(">> 0xdeadbeef 0x%x\n", secret - i + j);

    if (secret - i + j == 0xdeadbeef) {
        printf("You are the one. This must be the choice of Stacks Gate!\n");
        printf("Here is your flag: %s\n", FLAG);
    } else {
        printf("Begone, FBI Spy!\n");
    }

    exit(0);
}

int main() {

    gid_t gid = getegid();
    setresgid(gid, gid, gid);

    setbuf(stdout, NULL);

    srand(time(NULL));

    interview(0);

    return 0;
}