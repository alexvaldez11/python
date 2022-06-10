#programa de las n reinas
#ALGORITMO DE LAS VEGAS 

import random
import time 

n = 8
solucion = []
inicio_tiempo = time.time()

columna = [False]*n
diagonal_izq = [False]*(n*2)
diagonal_der = [False]*(n*2)

def disponibles(y,n):
    columnas_disponibles  = []
    for x in range(n):
        if(columna[x] or diagonal_izq[x+y] or diagonal_der[x-y+n-1]):
            #si la reina es atacada se debe volver a empezar 
            continue
        columnas_disponibles.append(x)
    return columnas_disponibles


while(len(solucion) != n and n>3 ):
    solucion = []
    columna =[False]*n
    diagonal_izq = [False]*(n*2)
    diagonal_der = [False]*(n*2)

    for y in range(n):
        #Colocar la reina en una columna aleatoria 
        columnas_d = disponibles(y, n);
        #solo si hay columnas no atacadas 
        if(columnas_d):
            x = random.choice(columnas_d)
        else:
            break
        columna[x]  = diagonal_izq[x+y] = diagonal_der[x-y+n-1] = True
        solucion.append((x,y))
end = time.time()
tiempo_total = end -inicio_tiempo
print(solucion)
print("\n Tomo %f segundos"% (tiempo_total))
















random.choice([1,2,3])
if ([]):
    print("y")
else:
    print("n")
