# About
This repository contains:
* Set of examples how to use [CLion](https://www.jetbrains.com/clion/) with various unsupported compilers using
  [Custom Defined Compiler](https://blog.jetbrains.com/clion/2021/10/clion-2021-3-eap-custom-compiler/) feature
 * [Public set of Custom Defined Compiler](configs) configuratuions

## Supported variants so far

* [CMake-Embarcadero-BCC32C](CMake-Embarcadero-BCC32C)
  * Build System: [CMake](https://cmake.org/)
  * Compiler: [Embarcadero Free C Compiler](https://www.embarcadero.com/free-tools/ccompiler)
    * Compiler definition file: [custom-compiler-bcc.yaml](CMake-Embarcadero-BCC32C/custom-compiler-bcc.yaml)
  * Host Platforms: Windows 32bit
  * Target Platform: Windows 32bit
* [CMake-Texas-Instruments-MSP430-CGT](CMake-Texas-Instruments-MSP430-CGT)
  * Build System: [CMake](https://cmake.org/)
  * Compiler: [TI MSP430 CGT compiler](https://www.ti.com/tool/MSP-CGT)
    * Compiler definition file: [custom-compiler-msp430.yaml](CMake-Texas-Instruments-MSP430-CGT/custom-compiler-msp430.yaml)
  * Host Platforms: Windows, Linux, Mac
  * Target Platform: MSP430 MCU
* [CMake-SDCC](CMake-SDCC)
  * Build System: [CMake](https://cmake.org/)
  * Compiler: [SDCC](http://sdcc.sourceforge.net/) for stm8
    * Compiler definition file: [custom-compiler-sdcc-stm8.yaml](CCMake-SDCC/custom-compiler-sdcc-stm8.yaml)
  * Host Platforms: Windows, Linux, Mac
  * Target Platform: STM8 MCU
  