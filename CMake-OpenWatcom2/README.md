## Custom compiler definitions for CLion and OpenWatcom 2

This compiler definition allows you to use OpenWatcom 2 from Linux or Windows.

## Supported platforms

- Windows NT (x86)
- 16-bit OS/2
- 32-bit OS/2
- DOS
- 32-bit DOS (using DOS/4GW)
- Linux (x86)

## Unsupported platforms

- 16-bit Windows: don't know how to make it work, patches welcome
- Windows for MIPS, PowerPC or Alpha: the compilers are there, but the libraries are not made, contribute to [Open Watcom 2](https://github.com/open-watcom/open-watcom-v2) to make it possible
- QNX: headers and libraries are copyright of BlackBerry Limited, ping them for opensourcing them (as they were for QNX 2 and QNX 4 probably not of much interest to them anymore?)
- NetWare: libraries are there but headers need to be installed separately, ping Micro Focus International for opensourcing them (as they abandoned NetWare long ago)
- Others: Watcom supported many targets over the ages and I don't know which others may just need some care to make them work

## Instructions

The most important step is to ensure that Watcom binaries are in the path. This depends on your exact installation but usually on Windows it is `C:\WATCOM\BINNT64` and on Linux it is `/opt/watcom/binl64`. Until JetBrains allow to specify APPENDING path members for a specific toolchain (tried with Environment Variables, no go) this is a must.

After this is done you need to add the compilers in `Settings -> Build, Execution, Deployment -> Toolchains` and set up at least the C compiler and C++ compiler (they're the same) and at least in Windows (as there's no system `make` to make CLion happy) also select `wmake` (`wmake.exe`).

Compiler for 16-bit targets: `wcl` or `wcl.exe`
Compiler for 32-bit targets: `wcl386` or `wcl386.exe`
Compiler for Alpha targets: `wclaxp` or `wclaxp.exe` *DOESN'T INCLUDE C OR C++ LIBRARIES*
Compiler for MIPS targets: `wclmps` or `wclmps.exe` *DOESN'T INCLUDE C OR C++ LIBRARIES*
Compiler for PowerPC targets: `wclppc` or `wclppc.exe` *DOESN'T INCLUDE C OR C++ LIBRARIES*

Then, for the project, you need to go `Settings -> Build, Execution, Deployment -> CMake` and create the appropriate targets.

In each target set the following environment for Windows (change paths appropriately if installed in another location):

- `WATCOM=C:\WATCOM`
- `INCLUDE=C:\WATCOM\H\;C:\WATCOM\H\NT\;C:\WATCOM\H\NT\DIRECTX\;C:\WATCOM\H\NT\DDK\;%INCLUDE%`

or in Linux (change paths appropriately if installed in another location):

- `WATCOM=/opt/watcom`
- `INCLUDE=/opt/watcom/lh`

then in CMake options you need to set: `-DCMAKE_SYSTEM_NAME=<system> -DCMAKE_SYSTEM_PROCESSOR=<arch> -G "Watcom WMake"`

where `<system>` is:

- `DOS` for DOS
- `OS2` for OS/2
- `Windows` for Windows and Windows NT
- `Linux` for Linux

and `<arch>` is:

- `I86` for 16-bit
- `I386` for 32-bit
- none for 32-bit or the others *(untested)*

## Final notes

The preprocessor macros have been a bestguess and may be severely incomplete, patches welcome!

2021 - [Natalia Portillo](https://github.com/claunia)
Many thanks to [Jiří Malák](https://github.com/jmalak) for keeping OpenWatcom alive!
