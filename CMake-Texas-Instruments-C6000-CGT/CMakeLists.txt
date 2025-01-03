cmake_minimum_required(VERSION 3.21)
set(CMAKE_SYSTEM_NAME Generic)
# Trick CMake that the compiler always works
set(CMAKE_C_COMPILER_WORKS 1)
set(CMAKE_CXX_COMPILER_WORKS 1)
# End of trick

project(CMake-Texas-Instruments-C6000-CGT C CXX ASM)

# CMake 3.21 does not support TI compilers well, we need to make a couple of workarounds
# Explicitly set include  and library directories
find_program(TOOLCHAIN_PATH ${CMAKE_C_COMPILER})

get_filename_component(TOOLCHAIN_PATH ${TOOLCHAIN_PATH} DIRECTORY) # Path to compiler
get_filename_component(TOOLCHAIN_PATH ${TOOLCHAIN_PATH} DIRECTORY) # To parent dir
message(STATUS "TOOLCHAIN_PATH: " ${TOOLCHAIN_PATH})

include_directories(${TOOLCHAIN_PATH}/include)
include_directories(${TOOLCHAIN_PATH}/include/libcxx)
add_link_options(--library=${TOOLCHAIN_PATH}/lib/lnk.cmd --search_path=${TOOLCHAIN_PATH}/lib)
# End of the workaround

message(STATUS "CMAKE_C_FLAGS: " ${CMAKE_C_FLAGS})
message(STATUS "CMAKE_CXX_FLAGS: " ${CMAKE_CXX_FLAGS})

set(CMAKE_EXPORT_COMPILE_COMMANDS ON)
set(CMAKE_C_STANDARD 99)

add_executable(custom-compiler-test main.cpp cmain.c test.asm)
target_compile_options(custom-compiler-test PRIVATE --check_misra=all -pdr --misra_advisory=remark)
set_source_files_properties(test.asm PROPERTIES LANGUAGE ASM)
