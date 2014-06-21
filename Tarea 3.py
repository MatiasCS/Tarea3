#Se inicializan estas variables para hacer mas facil el llenado de matrices
A=0
B=1
C=2
D=3
E=4
F=5
G=6
H=7
I=8


#Matriz de adyacencia
matriz_a_global=[]
#Matriz de costos
matriz_c=[]


#Crear inicializar matrices
for i in range(9):
    matriz_a_global.append([])
    for j in range(9):
        matriz_a_global[i].append(float("inf"))

for i in range(9):
    matriz_c.append([])
    for j in range(9):
        matriz_c[i].append(float("inf"))



#Input: Nodo al cual corresponde la tabla que se inicializara
#       Matriz_costo pertenece a la matriz de costo
#Output:Devuelve una matriz inicializado solo con el vector distancia del nodo

def inicializar_tablas(nodo,matriz_costo):
    matriz=[]
    for i in range(9):
        matriz.append([])
        for j in range(9):
            matriz[i].append(float("inf"))
    for i in range(9):
        matriz[nodo][i]=matriz_costo[nodo][i]
        matriz[nodo][nodo]=0
    return matriz

#Input: Nodo al cual se le quiere saber sus vecinos
#Output: Devuelve una lista con todos los vecinos de Nodo
def vecinos(nodo):
    vecinos=[]
    for i in range(9):
        if matriz_a_global[nodo][i]==1:
            vecinos.append(i)
    return vecinos


#Nodo es el router que envia su vector direccion
#Tabla 1 es la tabla del router1
#Tabla 2 es la tabla (router) que recibira el vector direccion
def enviar_vector(nodo,tabla1,tabla2):
    tabla2[nodo]=tabla1[nodo]

#Para a cada vecino se le envia el vector direccion de esa tabla.
def actualizar_tabla(tabla1,tablas):
    aux=0
    for i in range(len(tablas.keys())):
        if tablas.keys()[i]==tabla1:
            aux=tablas.keys()[i]
            for j in vecinos(int(aux)):
                enviar_vector(j,tablas[str(j)],tablas[tabla1])

#Algoritmo de bellmand ford que permite calcular el menor costo
#del nodo a su vecino.
def bellamnd_ford(nodo,tabla1):
    aux=[]
    aux=list(tabla1[int(nodo)])


    for i in range(len(tabla1[int(nodo)])):
        actual=tabla1[int(nodo)][int(i)]
        for j in  range(len(tabla1[int(nodo)])):
            escala=tabla1[int(nodo)][int(j)]
            for k in  range(len(tabla1[int(nodo)])):
                final=escala+tabla1[int(j)][int(k)]
                if(k==i and actual>final):
                    tabla1[int(nodo)][int(i)]=final

    if aux!=tabla1[int(nodo)]:
        return True
    else:
        return False


def modificar_vector_apariencia(lista):
    aux=[]
    for i in range(len(lista)):
        if lista[i]!=float('inf'):
            aux.append(str(nombres_global[str(i)])+":"+str(lista[i]))
    return aux

#Algoritmo que actuliz TODAS las tablas
def actualizar_todas_las_tablas():
    actualizar_tabla('0',tablas)
    actualizar_tabla("1",tablas)
    actualizar_tabla("2",tablas)
    actualizar_tabla("3",tablas)
    actualizar_tabla("4",tablas)
    actualizar_tabla("5",tablas)
    actualizar_tabla("6",tablas)
    actualizar_tabla("7",tablas)
    actualizar_tabla("8",tablas)


#Algoritmo que escribe en un txt el estado de la tabla del router Nodo
def mostrar_tabla(nodo,tabla,fichero):
    fichero.write("Tabla nodo: "+nombres_global[str(nodo)]+"\n")
    fichero.write("Vector Distancia de "+ nombres_global[str(nodo)] +"--->"+ str(modificar_vector_apariencia(tabla[nodo]))+"\n")
    for i in vecinos(int(nodo)):
        fichero.write("Vector Distancia de "+ nombres_global[str(i)]+"--->"+str(modificar_vector_apariencia(tabla[i]))+"\n")
    fichero.write("\n")

#Algoritmo que escribe en un txt el estado de TODAS las tablas
def mostrar_todas_las_tablas(f):
    mostrar_tabla(A,tabla_A,f)
    mostrar_tabla(B,tabla_B,f)
    mostrar_tabla(C,tabla_C,f)
    mostrar_tabla(D,tabla_D,f)
    mostrar_tabla(E,tabla_E,f)
    mostrar_tabla(F,tabla_F,f)
    mostrar_tabla(G,tabla_G,f)
    mostrar_tabla(H,tabla_H,f)
    mostrar_tabla(I,tabla_I,f)

#Inicializacion de matrices que sirven para rellenar las tablas de cada router.
#A
matriz_a_global[A][B],matriz_a_global[A][G],matriz_a_global[A][I]=1,1,1
matriz_c[A][B],matriz_c[A][G],matriz_c[A][I]=1,4,10

#B
matriz_a_global[B][A],matriz_a_global[B][C],matriz_a_global[B][E]=1,1,1
matriz_c[B][A],matriz_c[B][C],matriz_c[B][E]=1,9,8

#C
matriz_a_global[C][D],matriz_a_global[C][B]=1,1
matriz_c[C][D],matriz_c[C][B]=2,9

#D
matriz_a_global[D][C],matriz_a_global[D][F],matriz_a_global[D][E],matriz_a_global[D][I]=1,1,1,1
matriz_c[D][C],matriz_c[D][F],matriz_c[D][E],matriz_c[D][I]=2,4,9,2

#E
matriz_a_global[E][I],matriz_a_global[E][D],matriz_a_global[E][B],matriz_a_global[E][F]=1,1,1,1
matriz_c[E][I],matriz_c[E][D],matriz_c[E][B],matriz_c[E][F]=1,9,8,2

#F
matriz_a_global[F][H],matriz_a_global[F][E],matriz_a_global[F][D]=1,1,1
matriz_c[F][H],matriz_c[F][E],matriz_c[F][D]=6,2,4

#G
matriz_a_global[G][H],matriz_a_global[G][A]=1,1
matriz_c[G][H],matriz_c[G][A]=7,4

#H
matriz_a_global[H][I],matriz_a_global[H][F],matriz_a_global[H][G]=1,1,1
matriz_c[H][I],matriz_c[H][F],matriz_c[H][G]=3,6,7

#I
matriz_a_global[I][A],matriz_a_global[I][D],matriz_a_global[I][E],matriz_a_global[I][H]=1,1,1,1
matriz_c[I][A],matriz_c[I][D],matriz_c[I][E],matriz_c[I][H]=10,2,1,3

   
tabla_A=inicializar_tablas(A,matriz_c)
tabla_B=inicializar_tablas(B,matriz_c)
tabla_C=inicializar_tablas(C,matriz_c)
tabla_D=inicializar_tablas(D,matriz_c)
tabla_E=inicializar_tablas(E,matriz_c)
tabla_F=inicializar_tablas(F,matriz_c)
tabla_G=inicializar_tablas(G,matriz_c)
tabla_H=inicializar_tablas(H,matriz_c)
tabla_I=inicializar_tablas(I,matriz_c)

##Diccionario de tablas.
#RA = Router A
tablas={
    '0':tabla_A,
    '1':tabla_B,
    '2':tabla_C,
    '3':tabla_D,
    '4':tabla_E,
    '5':tabla_F,
    '6':tabla_G,
    '7':tabla_H,
    '8':tabla_I
    }

nombres_global={
    '0':'A',
    '1':'B',
    '2':'C',
    '3':'D',
    '4':'E',
    '5':'F',
    '6':'G',
    '7':'H',
    '8':'I'

    }


#######################################
########### ITERACION 1 ###############
contador=2
f=open("Redes parte 2.txt","w")

f.write("####################Iteracion 0 ###################################\n")
mostrar_todas_las_tablas(f)
f.write("####################Iteracion 1 ###################################\n")
actualizar_todas_las_tablas()
mostrar_todas_las_tablas(f)

#################################################################################
########### Aca se realiza el intercambio de vector de distancias ###############
#################################################################################
b1=True
b2=True
b3=True
b4=True
b5=True
b6=True
b7=True
b8=True

while (b1 or b2 or b3 or b4 or b5 or b6 or b7 or b8 or b9):
    f.write("####################Iteracion "+str(contador)+" ###################################\n")
    contador=contador+1
    
    b1=bellamnd_ford("0",tabla_A)
    b2=bellamnd_ford("1",tabla_B)
    b3=bellamnd_ford("2",tabla_C)
    b4=bellamnd_ford("3",tabla_D)
    b5=bellamnd_ford("4",tabla_E)
    b6=bellamnd_ford("5",tabla_F)
    b7=bellamnd_ford("6",tabla_G)
    b8=bellamnd_ford("7",tabla_H)
    b9=bellamnd_ford("8",tabla_I)

    actualizar_todas_las_tablas()
    mostrar_todas_las_tablas(f)
f.close()






##########################################################################
############### INICIO PARTE 3  ########################################
##########################################################################

#A
matriz_a_global[A][B],matriz_a_global[A][G],matriz_a_global[A][I]=1,1,1
matriz_c[A][B],matriz_c[A][G],matriz_c[A][I]=1,4,10

#B
matriz_a_global[B][A],matriz_a_global[B][C],matriz_a_global[B][E]=1,1,1
matriz_c[B][A],matriz_c[B][C],matriz_c[B][E]=1,9,8

#C
matriz_a_global[C][D],matriz_a_global[C][B]=1,1
matriz_c[C][D],matriz_c[C][B]=2,9

#D
matriz_a_global[D][C],matriz_a_global[D][F],matriz_a_global[D][E],matriz_a_global[D][I]=1,1,1,1
matriz_c[D][C],matriz_c[D][F],matriz_c[D][E],matriz_c[D][I]=2,4,9,2

#E
matriz_a_global[E][I],matriz_a_global[E][D],matriz_a_global[E][B],matriz_a_global[E][F]=1,1,1,1
matriz_c[E][I],matriz_c[E][D],matriz_c[E][B],matriz_c[E][F]=1,9,8,2

#F
matriz_a_global[F][H],matriz_a_global[F][E],matriz_a_global[F][D]=1,1,1
matriz_c[F][H],matriz_c[F][E],matriz_c[F][D]=6,2,4

#G
matriz_a_global[G][H],matriz_a_global[G][A]=1,1
matriz_c[G][H],matriz_c[G][A]=7,4

#H
matriz_a_global[H][F],matriz_a_global[H][G]=1,1
matriz_a_global[H][I]=0
matriz_c[H][F],matriz_c[H][G]=6,7
matriz_c[H][I]=float("inf")

#I
matriz_a_global[I][A],matriz_a_global[I][D],matriz_a_global[I][E]=1,1,1
matriz_a_global[I][H]=0
matriz_c[I][A],matriz_c[I][D],matriz_c[I][E]=10,2,1
matriz_c[I][H]=float("inf")

tabla_A=inicializar_tablas(A,matriz_c)
tabla_B=inicializar_tablas(B,matriz_c)
tabla_C=inicializar_tablas(C,matriz_c)
tabla_D=inicializar_tablas(D,matriz_c)
tabla_E=inicializar_tablas(E,matriz_c)
tabla_F=inicializar_tablas(F,matriz_c)
tabla_G=inicializar_tablas(G,matriz_c)
tabla_H=inicializar_tablas(H,matriz_c)
tabla_I=inicializar_tablas(I,matriz_c)

##Diccionario de tablas.
#RA = Router A
tablas={
    '0':tabla_A,
    '1':tabla_B,
    '2':tabla_C,
    '3':tabla_D,
    '4':tabla_E,
    '5':tabla_F,
    '6':tabla_G,
    '7':tabla_H,
    '8':tabla_I
    }

nombres_global={
    '0':'A',
    '1':'B',
    '2':'C',
    '3':'D',
    '4':'E',
    '5':'F',
    '6':'G',
    '7':'H',
    '8':'I'

    }


#######################################
########### ITERACION 1 ###############
contador=2
f=open("Redes parte 3.txt","w")

f.write("####################Iteracion 0 ###################################\n")
mostrar_todas_las_tablas(f)
f.write("####################Iteracion 1 ###################################\n")
actualizar_todas_las_tablas()
mostrar_todas_las_tablas(f)

#################################################################################
########### Aca se realiza el intercambio de vector de distancias ###############
#################################################################################
b1=True
b2=True
b3=True
b4=True
b5=True
b6=True
b7=True
b8=True

while (b1 or b2 or b3 or b4 or b5 or b6 or b7 or b8):
    f.write("####################Iteracion "+str(contador)+" ###################################\n")
    contador=contador+1
    b1=bellamnd_ford("0",tabla_A)
    b2=bellamnd_ford("1",tabla_B)
    b3=bellamnd_ford("2",tabla_C)
    b4=bellamnd_ford("3",tabla_D)
    b5=bellamnd_ford("4",tabla_E)
    b6=bellamnd_ford("5",tabla_F)
    b7=bellamnd_ford("6",tabla_G)
    b8=bellamnd_ford("7",tabla_H)
    b8=bellamnd_ford("8",tabla_I)
    actualizar_todas_las_tablas()
    mostrar_todas_las_tablas(f)
f.close()


