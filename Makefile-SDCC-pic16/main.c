#include <stdio.h>

int main() {
    printf("Hello, World!\n");
    return 0;
}
int __code i = 0;
#ifndef __SDCC_pic16
#  error "__SDCC_pic16 macro is expected to be defined"
#endif