#include <iostream>

#pragma message ("Compile C++")
extern "C" void c_main(void);

int main() {
    std::cout << "Hello, World, from C++!" << std::endl;
    c_main();
    return 0;
}
