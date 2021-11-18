# About
This repository contains:
* Set of examples how to use [CLion](https://www.jetbrains.com/clion/) with various unsupported compilers using
  [Custom Defined Compiler](https://blog.jetbrains.com/clion/2021/10/clion-2021-3-eap-custom-compiler/) feature
 * [Public set of Custom Defined Compiler](configs) configuratuions

## Disclaimer

All the repository content is provided on an "AS IS" basis, without warranties or conditions of any kind.

Contributors must have permission to contribute config files, either by ensuring that config files are open source or suitably licensed.

Please note that JetBrains does not provide the described compilers or required licenses. The use of third-party
compilers in CLion is subject to the licensing policies of their vendors.
All trademarks, logos and brand names are the property of their respective owners. All company, product and service
names used in this repository are for identification purposes only. Use of these names,trademarks and brands does not
imply endorsement.

## Supported variants so far

* [CMake-armcc](CMake-armcc)
  * Build System: [CMake](https://cmake.org/)
  * Compiler: [ARMCC](https://www2.keil.com/mdk5)
    * Compiler definition file: [custom-compiler-sdcc-stm8.yaml](CMake-armcc/custom-compiler-armcc.yaml)
  * Host Platforms: Windows
  * Target Platform: ARM MCU
* [CMake-Embarcadero-BCC32C](CMake-Embarcadero-BCC32C)
  * Build System: [CMake](https://cmake.org/)
  * Compiler: [Embarcadero Free C Compiler](https://www.embarcadero.com/free-tools/ccompiler)
    * Compiler definition file: [custom-compiler-bcc.yaml](CMake-Embarcadero-BCC32C/custom-compiler-bcc.yaml)
  * Host Platforms: Windows 32bit
  * Target Platform: Windows 32bit
* [CMake-OpenWatcom2](CMake-OpenWatcom2)
  * Build System: [CMake](https://cmake.org/)
  * Compiler: [Open Watcom 2](https://github.com/open-watcom/open-watcom-v2)
    * Compiler definition file: [openwatcom2.yaml](CMake-OpenWatcom2/openwatcom2.yaml)
  * Host Platforms: Windows, Linux
  * Target Platform: Windows NT, DOS, 32-bit DOS (DOS/4GW), 16-bit OS/2, 32-bit OS/2, Linux/x86
  * Contributed by: [Natalia Portillo](https://github.com/claunia)  
* [CMake-SDCC](CMake-SDCC)
  * Build System: [CMake](https://cmake.org/)
  * Compiler: [SDCC](http://sdcc.sourceforge.net/) for stm8
    * Compiler definition file: [custom-compiler-sdcc-stm8.yaml](CMake-SDCC/custom-compiler-sdcc-stm8.yaml)
  * Host Platforms: Windows, Linux, Mac
  * Target Platform: STM8 MCU
* [CMake-Texas-Instruments-MSP430-CGT](CMake-Texas-Instruments-MSP430-CGT)
  * Build System: [CMake](https://cmake.org/)
  * Compiler: [TI MSP430 CGT compiler](https://www.ti.com/tool/MSP-CGT)
    * Compiler definition file: [custom-compiler-msp430.yaml](CMake-Texas-Instruments-MSP430-CGT/custom-compiler-msp430.yaml)
  * Host Platforms: Windows, Linux, Mac
  * Target Platform: MSP430 MCU
* [Makefile-Tasking-Tricore](Makefile-Tasking-Tricore)
  * Build System: [Makefile](https://www.jetbrains.com/help/clion/makefiles-support.html)
  * Compilers: [TASKING VX-toolset for 8051, ARM Cortex, TriCore](https://www.tasking.com/)
    * Compiler definition file: [custom-compiler-tasking-generated.yaml](Makefile-Tasking-Tricore/custom-compiler-tasking-generated.yaml)
    * Compiler definition gathering script(Python): [custom_compiler_yaml_tasking.py](Makefile-Tasking-Tricore/custom_compiler_yaml_tasking.py)
  * Host Platforms: Windows, Linux
  * Target Platform: Infineon
  