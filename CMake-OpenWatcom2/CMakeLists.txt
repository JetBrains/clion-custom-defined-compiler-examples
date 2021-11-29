cmake_minimum_required(VERSION 3.21)

project(CMake-OpenWatcom2 C)

set(CMAKE_C_STANDARD 90)
# Target platform is NT
add_compile_options(-bt=nt)
add_executable(CMake-OpenWatcom2 main.c)
