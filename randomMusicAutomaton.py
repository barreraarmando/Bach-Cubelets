import sys
import random
from automaton import machines
from automaton.converters import pydot

SIL = 0
G3 = 8
Ab3 = 16
A3 = 24
Bb3 = 32
B3 = 40
C4 = 48
Db4 = 56
D4 = 64
Eb4 = 72
E4 = 80
F4 = 88
Gb4 = 96
G4 = 104
Ab4 = 112
A4 = 120
Bb4 = 128
B4 = 136
C5 = 144
Db5 = 152
D5 = 160
Eb5 = 168
E5 = 176
F5 = 184
Gb5 = 192
G5 = 200
Ab5 = 208
A5 = 216
Bb5 = 224
B5 = 232
C6 = 240
Db6 = 248

notas = [ ["SIL", 0], ["G3", 8], ["Ab3", 16], ["A3", 24], ["Bb3", 32], ["B3", 40], ["C4", 48],
    ["Db4", 56], ["D4", 64], ["Eb4", 72], ["E4", 80], ["F4", 88], ["Gb4", 96], ["G4", 104],
    ["Ab4", 112], ["A4", 120], ["Bb4", 128], ["B4", 136], ["C5", 144], ["Db5", 152], ["D5", 160],
    ["Eb5", 168], ["E5", 176], ["F5", 184], ["Gb5", 192], ["G5", 200], ["Ab5", 208], ["A5", 216],
    ["Bb5", 224], ["B5", 232], ["C6", 240], ["Db6", 248]
]
tonalidades = ['C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B']
tonalidadesNum = [48, 56, 64, 72, 80, 88, 96, 8, 16, 24, 32, 40]
intervalosMayor = [16, 16, 8, 16, 16, 16, 8]
intervalosMenor = [16, 8, 16, 16, 8, 16, 16]
intervalosMenorArmonica = [16, 8, 16, 16, 8, 24, 8]
duraciones = [["redonda", 8], ["blanca", 4], ["negra", 2], ["corchea", 1]]
probabilidades = [["negra", 50], ["blanca", 25], ["corchea", 25]]
numCompases = 8
numNotas = 32;
randomMelody = [];

m = machines.FiniteMachine()

def obtenerEscala(tonalidad, tipo):
    nota = tonalidadesNum[tonalidades.index(tonalidad)]
    escala = []
    escala.append(0)
    escala.append(nota)
    
    if (tipo == "major"):
        while (nota >= 8):
            for i in list(reversed(intervalosMayor)):
                nota = nota - i
                if (nota < 8):
                    break
                escala.append(nota)
        nota = tonalidadesNum[tonalidades.index(tonalidad)]
        while (nota < 256):
            for i in intervalosMayor:
                nota = nota + i
                if (nota > 255):
                    break
                escala.append(nota)
                
        escala.sort()
        return escala
    else:
        escalaMA = []
        escalaMA.append(0)
        escalaMA.append(nota)
        
        while (nota >= 8):
            for i in list(reversed(intervalosMenor)):
                nota = nota - i
                if (nota < 8):
                    break
                escala.append(nota)
        nota = tonalidadesNum[tonalidades.index(tonalidad)]
        while (nota < 256):
            for i in intervalosMenor:
                nota = nota + i
                if (nota > 255):
                    break
                escala.append(nota)
                
        nota = tonalidadesNum[tonalidades.index(tonalidad)]
        while (nota >= 8):
            for i in list(reversed(intervalosMenorArmonica)):
                nota = nota - i
                if (nota < 8):
                    break
                escalaMA.append(nota)
        nota = tonalidadesNum[tonalidades.index(tonalidad)]
        while (nota < 256):
            for i in intervalosMenorArmonica:
                nota = nota + i
                if (nota > 255):
                    break
                escalaMA.append(nota)
                
        escala.sort()
        escalaMA.sort()
        return escala, escalaMA 

def buscarNotaporBV(bv):
    for nota in notas:
        if (nota[1] == bv):
            return nota[0]
            break

def generarGrados(escala, tonalidad, tipo, escalaMA = None):
    grados = []
    
    if tipo == "major":
        I = []
        ii = []
        iii = []
        IV = []
        V = []
        vi = []
        vii = []
        grados = [I, ii, iii, IV, V, vi, vii]
        inicio = escala.index(tonalidadesNum[tonalidades.index(tonalidad)])
        
        i = inicio
        j = inicio
        contS = 1
        
        for cont, grado in enumerate(grados):
            if inicio > 1:
                j = j - 3
                while j > 0:
                    grado.append(escala[j])
                    if contS < 3:
                        j-=2
                    else:
                        j-=3
                        contS = 0
                    contS += 1  
                contS = 1
                j = inicio + cont + 1
            while i < len(escala):
                grado.append(escala[i])
                if contS < 3:
                    i+=2
                else:
                    i+=3
                    contS = 0
                contS += 1
            contS = 1
            i = inicio + cont + 1
            
            grado.sort()
            
    else:
        i = []
        ii = []
        III = []
        iv = []
        V = []
        VI = []
        VII = []
        vii = []
        grados = [i, ii, III, iv, V, VI, VII, vii]
        inicio = escala.index(tonalidadesNum[tonalidades.index(tonalidad)])
        
        i = inicio
        j = inicio
        contS = 1
        
        for cont, grado in enumerate(grados):
            if (cont == 4 or cont == 7):
                e = escalaMA
            else: 
                e = escala
            if inicio > 1:
                j = j - 3
                while j > 0:
                    grado.append(e[j])
                    if contS < 3:
                        j-=2
                    else:
                        j-=3
                        contS = 0
                    contS += 1  
                contS = 1
                if cont == 6:
                    j = inicio + cont
                else:
                    j = inicio + cont + 1
            while i < len(e):
                grado.append(e[i])
                if contS < 3:
                    i+=2
                else:
                    i+=3
                    contS = 0
                contS += 1
            contS = 1
            if cont == 6:
                i = inicio + cont
            else:
                i = inicio + cont + 1
            
            grado.sort()
        
    return grados

def buscarNotaCercana(lastNote, grado):
    mejorDif = 30
    
    if lastNote in grado:
        flag = False
        while (flag == False):
            cambioRandom = random.randint(-1, 1)
            notaIndex = grado.index(lastNote) + cambioRandom
            if not(notaIndex >= len(grado) or notaIndex < 0):
                flag = True
                return notaIndex
    else:
        nota = 0
        
        for notaC in grado:
            dif = abs(lastNote - notaC)
            if dif < mejorDif:
                mejorDif = dif
                nota = notaC
        
        return grado.index(nota)

def anadirNota(nota, valorR):
    if valorR == "corchea":
        duracion = 1
    elif valorR == "negra":
        duracion = 2
    elif valorR == "blanca":
        duracion = 4
        
    for i in range(duracion):        
        randomMelody.append(nota)
    
def generarMelodia(grado, tonalidad, escala, tipo, nombreGrado = "default"):
    n = len(grado)

    marca1 = len(randomMelody)
    
    if type(escala[0]) == list:
        escalaM = escala[0]
        escalaMA = escala[1]
        inicio = escalaM.index(tonalidadesNum[tonalidades.index(tonalidad)])
        final = escalaM.index(escalaM[-1])
    else:
        inicio = escala.index(tonalidadesNum[tonalidades.index(tonalidad)])
        final = escala.index(escala[-1])
    
    notasCompas = []
    primeraNota = False
    for i in range(4):
        if (len(randomMelody) == 0 or len(randomMelody) == numNotas-2) and primeraNota == False:
            primeraNota = True
            if (tipo == "major"):
                notasCompas.append(escala[inicio])
            else:
                notasCompas.append(escalaM[inicio])
        else:
            if i == 0 and primeraNota == False:
                lastNote = randomMelody[-1]
                notaIndex = buscarNotaCercana(lastNote, grado)
            else:
                lastNote = notasCompas[-1]
                flag = False
                while (flag == False):
                    cambioRandom = random.randint(-3, 3)
                    notaIndex = grado.index(lastNote) + cambioRandom
                    if not(notaIndex >= len(grado) or notaIndex < 0):
                        flag = True
            nota = grado[notaIndex]
            notasCompas.append(nota)

    
    #Determinar si la primera nota es blanca o negra
    if (random.randint(0, 100) > 75) or primeraNota == True:
        duracion1 = "blanca"
        anadirNota(notasCompas[0], "blanca")
    else:
        duracion1 = "negra"
        anadirNota(notasCompas[0], "negra")
        #Determinar si se coloca una nota de paso en el segundo pulso
        if (random.randint(0, 100) < 75):
            if (tipo == "major"):
                index1 = escala.index(notasCompas[0])
                index2 = escala.index(notasCompas[1])
                index3 = escala.index(notasCompas[2])
            else:
                if nombreGrado == 'V':
                    index1 = escalaMA.index(notasCompas[0])
                    index2 = escalaMA.index(notasCompas[1])
                    index3 = escalaMA.index(notasCompas[3])
                else:
                    index1 = escalaM.index(notasCompas[0])
                    index2 = escalaM.index(notasCompas[1])
                    index3 = escalaM.index(notasCompas[3])
            bigger = max(index1, index3)
            corcheas = False
            #Determinar si se coloca una nota auxiliar
            if index1 == index3:
                if (random.randint(0, 100) < 50):
                    notaIndex = min(index1 + 1, final)
                else:
                    notaIndex = max(index1 - 1, 0)
            elif abs(index1-index3) == 2:
                notaIndex = bigger - 1
            elif abs(index1-index3) == 3:
                corcheas = True
                notaIndex = bigger - 2
                notaIndex2 = bigger - 1
            else:
                notaIndex = index2
                
            #Anadir nota auxiliar o de paso
            if (tipo == "major"):
                nota = escala[notaIndex]
                if corcheas == True:
                    nota2 = escala[notaIndex2]
            else:
                if nombreGrado == 'V':
                    nota = escalaMA[notaIndex]
                    if corcheas == True:
                        nota2 = escalaMA[notaIndex2]
                else:
                    nota = escalaM[notaIndex]
                    if corcheas == True:
                        nota2 = escalaM[notaIndex2]
            if corcheas == False:
                anadirNota(nota, "negra")
            else:
                anadirNota(nota, "corchea")
                anadirNota(nota2, "corchea")
        else:
            anadirNota(notasCompas[1], "negra")
    
    #Determinar si la tercera nota es blanca o negra
    if (random.randint(0, 100) > 75):
        duracion3 = "blanca"
        anadirNota(notasCompas[2], "blanca")
    else:
        anadirNota(notasCompas[2], "negra")
        #Determinar si se coloca una nota de paso en el cuarto pulso
        if (random.randint(0, 100) < 75):
            if (tipo == "major"):
                index3 = escala.index(notasCompas[2])
            else:
                if nombreGrado == 'V':
                    index3 = escalaMA.index(notasCompas[3])
                else:
                    index3 = escalaM.index(notasCompas[3])
            if (random.randint(0, 100) < 50):
                notaIndex = min(index3 + 1, final)
            else:
                notaIndex = max(index3 - 1, 0)
                
            #Anadir nota auxiliar o de paso
            if (tipo == "major"):
                nota = escala[notaIndex]
            else:
                if nombreGrado == 'V':
                    nota = escalaMA[notaIndex]
                else:
                    nota = escalaM[notaIndex]
            anadirNota(nota, "negra")
        else:
            anadirNota(notasCompas[3], "negra")
    
    # Debug 
    """ 
    print("Notas del compas: ", end = "")
    for nota in notasCompas:
        print(buscarNotaporBV(nota), end = ", ")
    print("")


    print("Trozo de melodia: ")
    for i in range(marca1, len(randomMelody)):
        print(buscarNotaporBV(randomMelody[i]), end = ", ")
    print("")
    """
        

def main(argv):        
    n = len(argv)
    tonalidad = "G"
    tipo = "major"
    grados = []
    
    if n == 1:
        tonalidad = tonalidades[random.randint(0, 11)]
        if (random.randint(0, 1) == 0):
            tipo = "major"
        else:
            tipo = "minor"
    elif n == 2: 
        tonalidad = sys.argv[1]
        tipo = "major"
    elif n == 3:
        tonalidad = sys.argv[1]
        tipo = sys.argv[2]
    
    print("Generating melody on " + tonalidad + " " + tipo)
    
    if (tipo == "major"):
        escala = obtenerEscala(tonalidad, tipo)
        print("Escala natural :")
        for i in escala:
            print(buscarNotaporBV(i), end = ", ")
        grados = generarGrados(escala, tonalidad, tipo)
    else:
        escala, escalaMA = obtenerEscala(tonalidad, tipo)
        print("Escala natural :")
        for i in escala:
            print(buscarNotaporBV(i), end = ", ")
        print("\nEscala MA :")
        for i in escalaMA:
            print(buscarNotaporBV(i), end = ", ")   
        print("")
        grados = generarGrados(escala, tonalidad, tipo, escalaMA)
        escala = [escala, escalaMA]
        
    def direccionarGrado(new_state, triggered_event):
        if new_state == 'I':
            generarMelodia(grados[0], tonalidad, escala, tipo)
        if new_state == 'II':
            generarMelodia(grados[1], tonalidad, escala, tipo)
        if new_state == 'III':
            generarMelodia(grados[2], tonalidad, escala, tipo)
        if new_state == 'IV':
            generarMelodia(grados[3], tonalidad, escala, tipo)
        if new_state == 'V':
            generarMelodia(grados[4], tonalidad, escala, tipo)
        if new_state == 'VI':
            generarMelodia(grados[5], tonalidad, escala, tipo)
        if new_state == 'VII':
            generarMelodia(grados[6], tonalidad, escala, tipo)
    
    print("Grados armonicos:")
    for grado in grados:
        for i in grado:
            print(buscarNotaporBV(i), end = ", ")
        print("")
    print(escala)
    
    state_space = [
        {
            'name': 'I',
            'next_states': {
                'to_I': 'I',
                'to_II': 'II',
                'to_III': 'III',
                'to_IV': 'IV',
                'to_V': 'V',
                'to_VI': 'VI',
                'to_VII': 'VII',
            },
            'on_enter': direccionarGrado,
        },
        {
            'name': 'II',
            'next_states': {
                'to_I': 'I',
                'to_II': 'II',
                'to_III': 'III',
                'to_IV': 'IV',
                'to_V': 'V',
                'to_VI': 'VI',
                'to_VII': 'VII',
            },
            'on_enter': direccionarGrado,
        },
        {
            'name': 'III',
            'next_states': {
                'to_I': 'I',
                'to_II': 'II',
                'to_III': 'III',
                'to_IV': 'IV',
                'to_V': 'V',
                'to_VI': 'VI',
                'to_VII': 'VII',
            },
            'on_enter': direccionarGrado,
        },
        {
            'name': 'IV',
            'next_states': {
                'to_I': 'I',
                'to_II': 'II',
                'to_III': 'III',
                'to_IV': 'IV',
                'to_V': 'V',
                'to_VI': 'VI',
                'to_VII': 'VII',
            },
            'on_enter': direccionarGrado,
        },
        {
            'name': 'V',
            'next_states': {
                'to_I': 'I',
                'to_II': 'II',
                'to_III': 'III',
                'to_IV': 'IV',
                'to_V': 'V',
                'to_VI': 'VI',
                'to_VII': 'VII',
            },
            'on_enter': direccionarGrado,
        },
        {
            'name': 'VI',
            'next_states': {
                'to_I': 'I',
                'to_II': 'II',
                'to_III': 'III',
                'to_IV': 'IV',
                'to_V': 'V',
                'to_VI': 'VI',
                'to_VII': 'VII',
            },
            'on_enter': direccionarGrado,
        },
        {
            'name': 'VII',
            'next_states': {
                'to_I': 'I',
                'to_II': 'II',
                'to_III': 'III',
                'to_IV': 'IV',
                'to_V': 'V',
                'to_VI': 'VI',
                'to_VII': 'VII',
            },
            'on_enter': direccionarGrado,
        }
    ]
    
    m = machines.FiniteMachine.build(state_space)
    m.default_start_state = 'I'
    m.initialize()
    generarMelodia(grados[0], tonalidad, escala, tipo)
    
    print(m.pformat())
    #print(pydot.convert(m, "Automaton graph"))

    events = ['to_I', 'to_II', 'to_III', 'to_IV', 'to_V', 'to_VI', 'to_VII']
    
    print("=============")
    print("Current state => %s" % m.current_state)
    for i in range(numCompases-3):
        event = events[random.randint(0, len(events)-1)]
        m.process_event(event)
        print("=============")
        print("Current state => %s" % m.current_state)
    
    m.process_event('to_V')
    print("=============")
    print("Current state => %s" % m.current_state)
    print("=============")
    
    m.process_event('to_I')
    print("Current state => %s" % m.current_state)
    print("=============\n")
    
    print("Generated Melody:")
    #print("Numero de notas: " + str(len(randomMelody)))
    for nota in randomMelody:
        print(buscarNotaporBV(nota), end = ", ")
    print("")
    print("Values for Cubelet:")
    for nota in randomMelody:
        print(nota, end = ", ")
    

if __name__ == '__main__':
    main(sys.argv)
