CC = cctc
LD = ltc
BIN = build/
CFLAGS = -co
CPPFLAGS = -co

all: $(BIN)main.elf

.PHONY: create-build custom-compiler-yaml
create-build:
	-mkdir build

$(BIN)cmain.o: create-build cmain.c
	$(CC) $(CFLAGS) cmain.c -o $(BIN)cmain.o

$(BIN)main.o: create-build main.cpp
	$(CC) $(CPPFLAGS) main.cpp -o $(BIN)main.o

$(BIN)main.elf: $(BIN)cmain.o $(BIN)main.o
	$(LD) -o $(BIN)main.elf $(BIN)main.o $(BIN)cmain.o --map-file --munch -lcxxsx_fpu -lcpsx_fpu -lcsw_fpu -lfp_fpu -lrt -L"C:\Program Files\TASKING\TriCore v6.3r1\ctc\lib\tc13"

custom-compiler-yaml:
	$(CC) custom-compiler/empty.c -El

clean:
	del /Q build\\*.*

