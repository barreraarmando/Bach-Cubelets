#include "cubelet.h"
#include <stdbool.h>

#define FI1 96
#define SOL 104
#define LA 120
#define SI 136
#define DO 144
#define DI 152
#define RE 160
#define MI 176
#define FI 192
#define SOL2 200
#define LA2 216
#define SI2 232
#define SIL 0

int cont = 0;
int pieza[] = {SI2, SI2, SOL2, LA2, SI2, SOL2,
    LA2, LA2, RE, MI, FI, RE,
    SOL2, SOL2, MI, FI, SOL2, RE,
    DI, DI, SI, DI, LA, LA,
    LA, SI, DI, RE, MI, FI,
    SOL2, SOL2, FI, FI, MI, MI,
    FI, FI, LA, LA, DI, DI,
    RE, RE, RE, RE, RE, RE
};
int tempo = 250;
int retardo = 24000;
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
