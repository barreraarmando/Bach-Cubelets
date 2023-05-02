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
#define SIL 0x

int cont = 0;
int pieza[] = {RE, RE, SOL, LA, SI, DO,
    RE, RE, SOL, SIL, SOL, SIL,
    MI, MI, DO, RE, MI, FI,
    SOL2, SOL2, SOL, SIL, SOL, SIL,
    DO, DO, RE, DO, SI, LA,
    SI, SI, DO, SI, LA, SOL,
    FI1, FI1, SOL, LA, SI, SOL,
    SI, SI, LA, LA, LA, LA
};
int tempo = 250;
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

}

void loop() {
    set_interval(tempo, play);
    wait(36000);
}
