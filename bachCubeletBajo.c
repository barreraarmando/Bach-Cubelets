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
    SI, SI, SI, SI, SI, SI,
    DO, DO, DO, DO, DO, DO,
    SI, SI, SI, SI, SI, SI,
    LA, LA, LA, LA, LA, LA,
    SOL, SOL, SOL, SOL, SOL,
    RE, RE, SI, SI, SOL, SOL,
    RE, RE, RE, DO, SI, LA
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
