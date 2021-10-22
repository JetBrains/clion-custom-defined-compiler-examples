#include "main.h"
//
// Created by Ilia.Motornyi on 22-Oct-21.
//

extern "C" void cppMain(void);
void cppMain(void) {
    HAL_GPIO_TogglePin(LD3_GPIO_Port,LD3_Pin);
    HAL_Delay(450);
}
