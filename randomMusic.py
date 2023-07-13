import sys
import random

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
intervalosMenorArmonica = [16, 8, 16, 16, 8, 16, 24]
duraciones = [["redonda", 8], ["blanca", 4], ["negra", 2], ["corchea", 1]]
probabilidades = [["negra", 50], ["blanca", 25], ["corchea", 25]]
numNotas = 32;
randomMelody = [];

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
    else:
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
    
    escala.sort()
    
    return escala

def anadirNota(escala, valorR, nota = "default"):
    if valorR == "corchea":
        duracion = 1
    elif valorR == "negra":
        duracion = 2
    elif valorR == "blanca":
        duracion = 4
        
    for i in range(duracion):        
        if nota == "default":
            nota = escala[random.randint(0, len(escala)-1)]
        randomMelody.append(nota)

def generarMelodia(escala, tonalidad):
    i = 0
    valorR = "negra"
    
    while (i < numNotas*2):
        if (i == 0 or i >= (numNotas*2)-4):
            anadirNota(escala, "blanca", tonalidad)
            i = i + 4
        else:
            moneda = random.randint(0, 100)
            acumulador = 0
        
            for p in probabilidades:
                if (moneda >= acumulador and moneda <= (acumulador + p[1])):
                    valorR = p[0]
                    break
                acumulador = acumulador + p[1]
            anadirNota(escala, valorR)
            if valorR == "corchea":
                i = i + 1
            elif valorR == "negra":
                i = i + 2
            elif valorR == "blanca":
                i = i + 4
            
            
    print("Melody: \n")
    for i in randomMelody:
        print(str(i) + ", ", end = "")
    print("\n")
    
    print("Number of notes: " + str(len(randomMelody)))
    
    print("Notes: \n")
    for i in randomMelody:
        for j in notas:
            if (j[1] == i):
                print(j[0] + ", ", end = "")

def main(argv):
    n = len(argv)
    tonalidad = "G"
    tipo = "major"
    
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
    escala = obtenerEscala(tonalidad, tipo)
    generarMelodia(escala, tonalidadesNum[tonalidades.index(tonalidad)])

if __name__ == '__main__':
    main(sys.argv)
