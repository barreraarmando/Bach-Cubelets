#include "cubelet.h"
#include <stdbool.h>

#define SOL 8
#define LA 24
#define SI 40
#define DO 48
#define RE 64
#define MI 80
#define FI 96
#define SIL 0

int cont = 0;
int pieza[] = {SOL, SOL, SOL, SOL, LA, LA,
    SOL, SOL, SI, SI, SOL, SOL,
    DO, DO, DO, DO, DO, DO,
    SI, SI, DO, SI, LA, SOL,
    LA, LA, LA, LA, LA, LA,
    SOL, SOL, SOL, SOL, SI, SI,
    DO, DO, RE, RE, RE, RE,
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
