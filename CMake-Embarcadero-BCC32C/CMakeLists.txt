cmake_minimum_required(VERSION 3.21)

project(CMake-Embarcadero-BCC32C C CXX)

set(CMAKE_EXPORT_COMPILE_COMMANDS ON)
set(CMAKE_C_STANDARD 99)

add_link_options(-lGl -lGpr)
add_executable(CMake-Embarcadero-BCC32C main.cpp cmain.c)

