#include "cubelet.h"
#include <stdbool.h>

#define FI1 96
#define SOL 104
#define LA 120
#define SI 136
#define DO 144
#define RE 160
#define MI 176
#define FI 192
#define SOL2 200
#define SIL 0

int cont = 0;
int pieza[] = {RE, RE, SOL, LA, SI, DO,
    RE, RE, SOL, SIL, SOL, SIL,
    MI, MI, DO, RE, MI, FI,
    SOL2, SOL2, SOL, SIL, SOL, SIL,
    DO, DO, RE, DO, SI, LA,
    SI, SI, DO, SI, LA, SOL,
    LA, LA, SI, LA, SOL, FI1,
    SOL, SOL, SOL, SOL, SOL, SOL
};
int tempo = 250;
int retardo = 12000;
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
