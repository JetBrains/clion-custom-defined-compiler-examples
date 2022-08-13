#   Trivial project
all: main.c
	sdcc -mpic16 --use-non-free -S main.c

gather_info:
#   List directories
	sdcc -mpic16 --use-non-free --print-search-dirs -E void.c
#   Create a void C file
	echo //void > void.c
#   List predefined macros
	sdcc -mpic16 --use-non-free -E -dM void.c
