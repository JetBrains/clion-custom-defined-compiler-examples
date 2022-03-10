cmake_minimum_required(VERSION 3.21)
set(CMAKE_SYSTEM_NAME Generic)
set(CMAKE_SYSTEM_VERSION 1)

set(CPU Cortex-M4)

set(CMAKE_C_FLAGS "--cpu=${CPU}  --c99")
set(CMAKE_CXX_FLAGS "--cpu=${CPU} --cpp11")
set(CMAKE_ASM_FLAGS "--cpu=${CPU} -c")

project(CMake-armcc C CXX ASM)

add_compile_options(--thumb)

include_directories(
        Core/Inc
        Drivers/CMSIS/Include
        Drivers/CMSIS/Core/Include
        Drivers/CMSIS/Device/ST/STM32L4xx/Include
        Drivers/STM32L4xx_HAL_Driver/Inc
        Drivers/STM32L4xx_HAL_Driver/Inc/Legacy
)
add_compile_definitions(DUSE_HAL_DRIVER STM32L432xx STM32_THREAD_SAFE_STRATEGY=2)
add_compile_definitions(__EVAL)

add_link_options(--branchpatch=sdcomp-29491-629360 --strict --summary_stderr --info sizes,totals,unused,veneers --load_addr_map_info --xref --callgraph --symbols)
add_link_options(--scatter=${CMAKE_SOURCE_DIR}/MDK-ARM/CMake-armcc.CMake-armcc.sct)
add_compile_options(--apcs=interwork --split_sections)

add_executable(${PROJECT_NAME})
target_sources(${PROJECT_NAME} PRIVATE
        Core/Src/main.c
        Core/Src/cppmain.cpp
        Core/Src/stm32l4xx_it.c
        Core/Src/stm32l4xx_hal_msp.c
        Core/Src/system_stm32l4xx.c
        MDK-ARM/armlib_lock_glue.c
        MDK-ARM/startup_stm32l432xx.s
        Drivers/STM32L4xx_HAL_Driver/Src/stm32l4xx_hal_tim.c
        Drivers/STM32L4xx_HAL_Driver/Src/stm32l4xx_hal_tim_ex.c
        Drivers/STM32L4xx_HAL_Driver/Src/stm32l4xx_hal_uart.c
        Drivers/STM32L4xx_HAL_Driver/Src/stm32l4xx_hal_uart_ex.c
        Drivers/STM32L4xx_HAL_Driver/Src/stm32l4xx_hal.c
        Drivers/STM32L4xx_HAL_Driver/Src/stm32l4xx_hal_i2c.c
        Drivers/STM32L4xx_HAL_Driver/Src/stm32l4xx_hal_i2c_ex.c
        Drivers/STM32L4xx_HAL_Driver/Src/stm32l4xx_hal_rcc.c
        Drivers/STM32L4xx_HAL_Driver/Src/stm32l4xx_hal_rcc_ex.c
        Drivers/STM32L4xx_HAL_Driver/Src/stm32l4xx_hal_flash.c
        Drivers/STM32L4xx_HAL_Driver/Src/stm32l4xx_hal_flash_ex.c
        Drivers/STM32L4xx_HAL_Driver/Src/stm32l4xx_hal_flash_ramfunc.c
        Drivers/STM32L4xx_HAL_Driver/Src/stm32l4xx_hal_gpio.c
        Drivers/STM32L4xx_HAL_Driver/Src/stm32l4xx_hal_dma.c
        Drivers/STM32L4xx_HAL_Driver/Src/stm32l4xx_hal_dma_ex.c
        Drivers/STM32L4xx_HAL_Driver/Src/stm32l4xx_hal_pwr.c
        Drivers/STM32L4xx_HAL_Driver/Src/stm32l4xx_hal_pwr_ex.c
        Drivers/STM32L4xx_HAL_Driver/Src/stm32l4xx_hal_cortex.c
        Drivers/STM32L4xx_HAL_Driver/Src/stm32l4xx_hal_exti.c
        )

set(HEX_FILE ${PROJECT_BINARY_DIR}/${PROJECT_NAME}.hex)
set(BIN_FILE ${PROJECT_BINARY_DIR}/${PROJECT_NAME}.bin)

add_custom_command(TARGET ${PROJECT_NAME} POST_BUILD
        COMMAND ${ARMCC_FROMELF} --text -z $<TARGET_FILE:${PROJECT_NAME}>
        COMMENT "Print memory info")
add_custom_command(TARGET ${PROJECT_NAME} POST_BUILD
        COMMAND ${ARMCC_FROMELF} --output ${HEX_FILE} --i32 $<TARGET_FILE:${PROJECT_NAME}>
        COMMAND ${ARMCC_FROMELF} --output ${BIN_FILE} --bin $<TARGET_FILE:${PROJECT_NAME}>
        COMMENT "Building ${HEX_FILE} and ${BIN_FILE}")
