#include "cubelet.h"
#include <stdbool.h>

#define RE1 64
#define MI1 80
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
int pieza[] = {RE, RE, SOL, FI1, SOL, SOL,
    MI, MI, SOL, FI1, SOL, SOL,
    RE, RE, DO, DO, SI, SI,
    LA, SOL, FI1, SOL, LA, LA,
    RE1, MI1, FI1, SOL, LA, SI,
    DO, DO, SI, SI, LA, LA,
    SI, RE, SOL, SOL, FI1, FI1,
    SOL, SOL, SOL, SOL, SOL, SOL
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
