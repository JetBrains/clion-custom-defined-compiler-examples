cmake_minimum_required(VERSION 3.21)
set(CMAKE_SYSTEM_NAME Generic)
# Trick CMake that the compiler always works
set(CMAKE_C_COMPILER_WORKS 1)
set(CMAKE_CXX_COMPILER_WORKS 1)
# End of trick

project(CMake-Texas-Instruments-MSP430-CGT C CXX)

# CMake 3.21 does not support TI compilers well, we need to make a couple of workarounds
# Explicitly set include  and library directories
find_program(TOOLCHAIN_PATH ${CMAKE_C_COMPILER})
get_filename_component(TOOLCHAIN_PATH ${TOOLCHAIN_PATH} DIRECTORY)
get_filename_component(TOOLCHAIN_PATH ${TOOLCHAIN_PATH} DIRECTORY)
include_directories(${TOOLCHAIN_PATH}/include)
include_directories(${TOOLCHAIN_PATH}/include/libcxx)
add_link_options(--library=${TOOLCHAIN_PATH}/lib/lnkx.cmd --search_path=${TOOLCHAIN_PATH}/lib)
# End of the workaround

set(CMAKE_EXPORT_COMPILE_COMMANDS ON)
set(CMAKE_C_STANDARD 99)
set_source_files_properties(PROPERTIES LANGUAGE CXX)

add_executable(custom-compiler-test main.cpp cmain.c )

