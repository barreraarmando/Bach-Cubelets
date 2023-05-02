#include "cubelet.h"
#include <stdbool.h>

#define SOL 8
#define LA 24
#define SI 40
#define DO 48
#define RE 64
#define MI 80
#define FI 96
#define SOL2 104
#define LA2 120
#define SI2 136
#define DO2 144
#define DI2 152
#define RE2 160
#define MI2 176
#define FI2 192
#define SIL 0

int cont = 0;
int pieza[] = {SI, SI, RE, RE, SI, SI,
    DO, DO, MI, MI, DO, DO,
    SI, SI, LA, LA, SOL, SOL,
    RE, RE, RE, RE, SIL, SIL,
    RE, RE, RE, RE, FI, FI,
    MI, MI, SOL2, SOL2, FI, FI,
    SOL2, SOL2, SI, SI, RE, RE,
    SOL2, SOL2, RE, RE, SOL, SOL
};
int tempo = 250;
int retardo = 36000;
int size = sizeof(pieza) / sizeof(int);

void play(void){
    if (cont >= size){
        clear_interval();
        cont = 0;
        block_value = 0;
        set_actuator_value(block_value);
    }
    else{
        block_value = pieza[cont];
        set_actuator_value(block_value);
        cont = cont + 1;
    }
}


void setup() {
    wait(retardo);
}

void loop() {
    set_interval(tempo, play);
    wait(36000);
}
