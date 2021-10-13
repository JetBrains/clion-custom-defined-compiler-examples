#include <stdio.h>

#pragma message ("Compile C")
int getInt();
long long fn() {
    return 3ll;
}

void fan(unsigned int x) {
    const int res = x == 123;
    if (x == 456) {}
}

int main() {
    puts("Hello, World from C!");
    return 0;
}

int putchar(int c) {
    //fake function
    return 1;
}
