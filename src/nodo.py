'''
Created on 29/04/2010

@author: lporras
'''
import copy

cubo_ordenado=[[ [ 0,0,0 ],
                 [ 0,0,0 ],
                 [ 0,0,0 ] ],
               [ [ 1,1,1 ],
                 [ 1,1,1 ],
                 [ 1,1,1 ] ],
               [ [ 2,2,2 ],
                 [ 2,2,2 ],
                 [ 2,2,2 ] ],
               [ [ 3,3,3 ],
                 [ 3,3,3 ],
                 [ 3,3,3 ] ],
               [ [ 4,4,4 ],
                 [ 4,4,4 ],
                 [ 4,4,4 ] ],
               [ [ 5,5,5 ],
                 [ 5,5,5 ],
                 [ 5,5,5 ] ]]

def cubete_1(cubo_actual):
    if(cubo_actual[2][0][0]==2 and cubo_actual[1][0][2]==1 and cubo_actual[0][2][0]==0):
        return 0
    return 1

def obtener_cubete_1(cubo_actual):
    lista=[]
    lista.append(cubo_actual[2][0][0])
    lista.append(cubo_actual[1][0][2])
    lista.append(cubo_actual[0][2][0])
    return lista

def cubete_2(cubo_actual):    
    if(cubo_actual[2][0][1]==2 and cubo_actual[0][2][1]==0):
        return 0
    return 1

def obtener_cubete_2(cubo_actual):
    lista=[]
    lista.append(cubo_actual[2][0][1])
    lista.append(cubo_actual[0][2][1])
    return lista

def cubete_3(cubo_actual):    
    if(cubo_actual[2][0][2]==2 and cubo_actual[0][2][2]==0 and cubo_actual[3][0][0]==3):
        return 0
    return 1

def obtener_cubete_3(cubo_actual):
    lista=[]
    lista.append(cubo_actual[2][0][2])
    lista.append(cubo_actual[0][2][2])
    lista.append(cubo_actual[3][0][0])
    return lista

def cubete_4(cubo_actual):    
    if(cubo_actual[2][1][0]==2 and cubo_actual[1][1][2]==1):
        return 0
    return 1

def obtener_cubete_4(cubo_actual):
    lista=[]
    lista.append(cubo_actual[2][1][0])
    lista.append(cubo_actual[1][1][2])
    return lista

def cubete_5(cubo_actual):    
    if(cubo_actual[2][1][2]==2 and cubo_actual[3][1][0]==3):
        return 0
    return 1

def obtener_cubete_5(cubo_actual):
    lista=[]
    lista.append(cubo_actual[2][1][2])
    lista.append(cubo_actual[3][1][0])
    return lista

def cubete_6(cubo_actual):    
    if(cubo_actual[1][2][2]==1 and cubo_actual[2][2][0]==2 and cubo_actual[4][0][0]==4):
        return 0
    return 1

def obtener_cubete_6(cubo_actual):
    lista=[]
    lista.append(cubo_actual[1][2][2])
    lista.append(cubo_actual[2][2][0])
    lista.append(cubo_actual[4][0][0])
    return lista

def cubete_7(cubo_actual):    
    if(cubo_actual[2][2][1]==2 and cubo_actual[4][0][1]==4):
        return 0
    return 1

def obtener_cubete_7(cubo_actual):
    lista=[]
    lista.append(cubo_actual[2][2][1])
    lista.append(cubo_actual[4][0][1])
    return lista

def cubete_8(cubo_actual):    
    if(cubo_actual[2][2][2]==2 and cubo_actual[4][0][2]==4 and cubo_actual[3][2][0]==3):
        return 0
    return 1

def obtener_cubete_8(cubo_actual):
    lista=[]
    lista.append(cubo_actual[2][2][2])
    lista.append(cubo_actual[4][0][2])
    lista.append(cubo_actual[3][2][0])
    return lista

def cubete_9(cubo_actual):    
    if(cubo_actual[0][1][0]==0 and cubo_actual[1][0][1]==1):
        return 0
    return 1

def obtener_cubete_9(cubo_actual):
    lista=[]
    lista.append(cubo_actual[0][1][0])
    lista.append(cubo_actual[1][0][1])
    return lista

def cubete_10(cubo_actual):    
    if(cubo_actual[0][1][2]==0 and cubo_actual[3][0][1]==3):
        return 0
    return 1

def obtener_cubete_10(cubo_actual):
    lista=[]
    lista.append(cubo_actual[0][1][2])
    lista.append(cubo_actual[3][0][1])
    return lista

def cubete_11(cubo_actual):    
    if(cubo_actual[4][1][0]==4 and cubo_actual[1][2][1]==1):
        return 0
    return 1

def obtener_cubete_11(cubo_actual):
    lista=[]
    lista.append(cubo_actual[4][1][0])
    lista.append(cubo_actual[1][2][1])
    return lista

def cubete_12(cubo_actual):    
    if(cubo_actual[4][1][2]==4 and cubo_actual[3][2][1]==3):
        return 0
    return 1

def obtener_cubete_12(cubo_actual):
    lista=[]
    lista.append(cubo_actual[4][1][2])
    lista.append(cubo_actual[3][2][1])
    return lista

def cubete_13(cubo_actual):    
    if(cubo_actual[0][0][0]==0 and cubo_actual[1][0][0]==1 and cubo_actual[5][0][2]==5):
        return 0
    return 1

def obtener_cubete_13(cubo_actual):
    lista=[]
    lista.append(cubo_actual[0][0][0])
    lista.append(cubo_actual[1][0][0])
    lista.append(cubo_actual[5][0][2])
    return lista

def cubete_14(cubo_actual):    
    if(cubo_actual[0][0][1]==0 and cubo_actual[5][0][1]==5):
        return 0
    return 1

def obtener_cubete_14(cubo_actual):
    lista=[]
    lista.append(cubo_actual[0][0][1])
    lista.append(cubo_actual[5][0][1])
    return lista

def cubete_15(cubo_actual):    
    if(cubo_actual[0][0][2]==0 and cubo_actual[3][0][2]==3 and cubo_actual[5][0][0]==5):
        return 0
    return 1

def obtener_cubete_15(cubo_actual):
    lista=[]
    lista.append(cubo_actual[0][0][2])
    lista.append(cubo_actual[3][0][2])
    lista.append(cubo_actual[5][0][0])
    return lista

def cubete_16(cubo_actual):    
    if(cubo_actual[1][1][0]==1 and cubo_actual[5][1][2]==5):
        return 0
    return 1

def obtener_cubete_16(cubo_actual):
    lista=[]
    lista.append(cubo_actual[1][1][0])
    lista.append(cubo_actual[5][1][2])
    return lista

def cubete_17(cubo_actual):    
    if(cubo_actual[3][1][2]==3 and cubo_actual[5][1][0]==5):
        return 0
    return 1

def obtener_cubete_17(cubo_actual):
    lista=[]
    lista.append(cubo_actual[3][1][2])
    lista.append(cubo_actual[5][1][0])
    return lista

def cubete_18(cubo_actual):    
    if(cubo_actual[1][2][0]==1 and cubo_actual[4][2][0]==4 and cubo_actual[5][2][2]==5):
        return 0
    return 1

def obtener_cubete_18(cubo_actual):
    lista=[]
    lista.append(cubo_actual[1][2][0])
    lista.append(cubo_actual[4][2][0])
    lista.append(cubo_actual[5][2][2])
    return lista

def cubete_19(cubo_actual):    
    if(cubo_actual[4][2][1]==4 and cubo_actual[5][2][1]==5):
        return 0
    return 1

def obtener_cubete_19(cubo_actual):
    lista=[]
    lista.append(cubo_actual[4][2][1])
    lista.append(cubo_actual[5][2][1])
    return lista

def cubete_20(cubo_actual):    
    if(cubo_actual[3][2][2]==3 and cubo_actual[4][2][2]==4 and cubo_actual[5][2][0]==5):
        return 0
    return 1

def obtener_cubete_20(cubo_actual):
    lista=[]
    lista.append(cubo_actual[3][2][2])
    lista.append(cubo_actual[4][2][2])
    lista.append(cubo_actual[5][2][0])
    return lista

def contar_cubetes_desordenados(cubo):
    contador = cubete_1(cubo)+ cubete_2(cubo)+ cubete_3(cubo)+ cubete_4(cubo) \
    + cubete_5(cubo)+ cubete_6(cubo)+ cubete_7(cubo)+ cubete_8(cubo)+ cubete_9(cubo) \
    + cubete_10(cubo)+ cubete_11(cubo)+ cubete_12(cubo)+ cubete_13(cubo)+ cubete_14(cubo) \
    + cubete_15(cubo)+ cubete_16(cubo)+ cubete_17(cubo)+ cubete_18(cubo)+ cubete_19(cubo) \
    + cubete_20(cubo)

    return contador

def numero_cubetes_desordenados_por_movimiento(cubo, script):
    contador = 0
    if(script == 'f' or script == 'F'):
        contador = cubete_1(cubo)+ cubete_2(cubo)+ cubete_3(cubo)+ cubete_4(cubo)+ cubete_5(cubo) \
        + cubete_6(cubo)+ cubete_7(cubo)+ cubete_8(cubo)  
    elif(script == 'b' or script == 'B'):
        contador = cubete_13(cubo)+ cubete_14(cubo)+ cubete_15(cubo)+ cubete_16(cubo)+ cubete_17(cubo) \
        + cubete_18(cubo)+ cubete_19(cubo)+ cubete_20(cubo)
    elif(script == 'u' or script == 'U'):
        contador = cubete_1(cubo)+ cubete_2(cubo)+ cubete_3(cubo)+ cubete_9(cubo)+ cubete_10(cubo) \
        + cubete_13(cubo)+ cubete_14(cubo)+ cubete_15(cubo)
    elif(script == 'd' or script == 'D'):
        contador = cubete_6(cubo)+ cubete_7(cubo)+ cubete_8(cubo)+ cubete_11(cubo)+ cubete_12(cubo) \
        + cubete_18(cubo)+ cubete_19(cubo)+ cubete_20(cubo)
    elif(script == 'l' or script == 'L'):
        contador = cubete_1(cubo)+ cubete_4(cubo)+ cubete_6(cubo)+ cubete_9(cubo)+ cubete_11(cubo) \
        + cubete_13(cubo)+ cubete_16(cubo)+ cubete_18(cubo)
    elif(script == 'r' or script == 'R'):
        contador = cubete_3(cubo)+ cubete_5(cubo)+ cubete_8(cubo)+ cubete_10(cubo)+ cubete_12(cubo) \
        + cubete_15(cubo)+ cubete_17(cubo)+ cubete_20(cubo)
            
    return contador


def asignar_cubo(script,cubo_actual):
    cubo = copy.deepcopy(cubo_actual)
    for i in range(len(script)):
        movimiento=script[int(i):int(i+1)]
            
        if(movimiento=='f'):
            movimiento_f(cubo)            
        elif(movimiento=='F'):
            movimiento_F(cubo)
        elif(movimiento=='b'):
            movimiento_b(cubo)
        elif(movimiento=='B'):
            movimiento_B(cubo)
        elif(movimiento=='d'):
            movimiento_d(cubo)
        elif(movimiento=='D'):
            movimiento_D(cubo)        
        elif(movimiento=='r'):
            movimiento_r(cubo)
        elif(movimiento=='R'):
            movimiento_R(cubo)
        elif(movimiento=='l'):
            movimiento_l(cubo)
        elif(movimiento=='L'):
            movimiento_L(cubo)
        elif(movimiento=='u'):
            movimiento_u(cubo)
        elif(movimiento=='U'):
            movimiento_U(cubo)
    return cubo

def rotacion_cara_derecha(valor_cara,cubo):

    temporal=cubo[valor_cara][0][0]
    
    cubo[valor_cara][0][0]=cubo[valor_cara][2][0]
    cubo[valor_cara][2][0]=cubo[valor_cara][2][2]
    cubo[valor_cara][2][2]=cubo[valor_cara][0][2]
    cubo[valor_cara][0][2]=temporal
    
    temporal=cubo[valor_cara][0][1]
    
    cubo[valor_cara][0][1]=cubo[valor_cara][1][0]
    cubo[valor_cara][1][0]=cubo[valor_cara][2][1]
    cubo[valor_cara][2][1]=cubo[valor_cara][1][2]
    cubo[valor_cara][1][2]=temporal
    

def rotacion_cara_izquierda(valor_cara,cubo):

    temporal=cubo[valor_cara][0][0]
    
    cubo[valor_cara][0][0]=cubo[valor_cara][0][2]
    cubo[valor_cara][0][2]=cubo[valor_cara][2][2]
    cubo[valor_cara][2][2]=cubo[valor_cara][2][0]
    cubo[valor_cara][2][0]=temporal
    
    temporal=cubo[valor_cara][0][1]
    
    cubo[valor_cara][0][1]=cubo[valor_cara][1][2]
    cubo[valor_cara][1][2]=cubo[valor_cara][2][1]
    cubo[valor_cara][2][1]=cubo[valor_cara][1][0]
    cubo[valor_cara][1][0]=temporal

def movimiento_f(cubo):
    
    lista_mov_temporal=copy.deepcopy(cubo[0][2])

    cubo[0][2][0]=cubo[3][0][0]
    cubo[0][2][1]=cubo[3][1][0]
    cubo[0][2][2]=cubo[3][2][0]
    
    cubo[3][0][0]=cubo[4][0][2]
    cubo[3][1][0]=cubo[4][0][1]
    cubo[3][2][0]=cubo[4][0][0]
    
    cubo[4][0][0]=cubo[1][0][2]
    cubo[4][0][1]=cubo[1][1][2]
    cubo[4][0][2]=cubo[1][2][2]
    
    cubo[1][0][2]=lista_mov_temporal[2]
    cubo[1][1][2]=lista_mov_temporal[1]
    cubo[1][2][2]=lista_mov_temporal[0]
    
    rotacion_cara_izquierda(2,cubo)
        
    #print cubo

def movimiento_F(cubo):
    lista_mov_temporal=copy.deepcopy(cubo[0][2])
    #print lista_mov_temporal 

    cubo[0][2][0]=cubo[1][2][2]
    cubo[0][2][1]=cubo[1][1][2]
    cubo[0][2][2]=cubo[1][0][2]
    
    cubo[1][2][2]=cubo[4][0][2]
    cubo[1][1][2]=cubo[4][0][1]
    cubo[1][0][2]=cubo[4][0][0]
    
    cubo[4][0][0]=cubo[3][2][0]
    cubo[4][0][1]=cubo[3][1][0]
    cubo[4][0][2]=cubo[3][0][0]

    cubo[3][2][0]=lista_mov_temporal[2]
    cubo[3][1][0]=lista_mov_temporal[1]
    cubo[3][0][0]=lista_mov_temporal[0]
    
    rotacion_cara_derecha(2,cubo)
            
    #print cubo
    
def movimiento_b(cubo):
    
    lista_mov_temporal=copy.deepcopy(cubo[0][0])

    cubo[0][0][0]=cubo[1][2][0]
    cubo[0][0][1]=cubo[1][1][0]
    cubo[0][0][2]=cubo[1][0][0]
    
    cubo[1][2][0]=cubo[4][2][2]
    cubo[1][1][0]=cubo[4][2][1]
    cubo[1][0][0]=cubo[4][2][0]
    
    cubo[4][2][2]=cubo[3][0][2]
    cubo[4][2][1]=cubo[3][1][2]
    cubo[4][2][0]=cubo[3][2][2]
    
    cubo[3][0][2]=lista_mov_temporal[0]
    cubo[3][1][2]=lista_mov_temporal[1]
    cubo[3][2][2]=lista_mov_temporal[2]
    
    rotacion_cara_izquierda(5,cubo)    
        
def movimiento_B(cubo):

    lista_mov_temporal=copy.deepcopy(cubo[0][0])

    cubo[0][0][0]=cubo[3][0][2]
    cubo[0][0][1]=cubo[3][1][2]
    cubo[0][0][2]=cubo[3][2][2]
    
    cubo[3][0][2]=cubo[4][2][2]
    cubo[3][1][2]=cubo[4][2][1]
    cubo[3][2][2]=cubo[4][2][0]
    
    cubo[4][2][2]=cubo[1][2][0]
    cubo[4][2][1]=cubo[1][1][0]
    cubo[4][2][0]=cubo[1][0][0]
    
    cubo[1][2][0]=lista_mov_temporal[0]
    cubo[1][1][0]=lista_mov_temporal[1]
    cubo[1][0][0]=lista_mov_temporal[2]
    
    rotacion_cara_derecha(5,cubo)

def movimiento_d(cubo):

    lista_mov_temporal = copy.deepcopy(cubo[2][2])
    #lista_mov_temporal.append(cubo[2][2][0])
    #lista_mov_temporal.append(cubo[2][2][1])
    #lista_mov_temporal.append(cubo[2][2][2])

    cubo[2][2][0]=cubo[3][2][0]
    cubo[2][2][1]=cubo[3][2][1]
    cubo[2][2][2]=cubo[3][2][2]
    
    cubo[3][2][0]=cubo[5][0][2]
    cubo[3][2][1]=cubo[5][0][1]
    cubo[3][2][2]=cubo[5][0][0]
    
    cubo[5][0][2]=cubo[1][2][0]
    cubo[5][0][1]=cubo[1][2][1]
    cubo[5][0][0]=cubo[1][2][2]
    
    cubo[1][2][0]=lista_mov_temporal[0]
    cubo[1][2][1]=lista_mov_temporal[1]
    cubo[1][2][2]=lista_mov_temporal[2]
    
    rotacion_cara_izquierda(4,cubo)
        
    #print cubo
    
def movimiento_D(cubo):

    lista_mov_temporal = copy.deepcopy(cubo[2][2])
    #lista_mov_temporal.append(cubo[2][2][0])
    #lista_mov_temporal.append(cubo[2][2][1])
    #lista_mov_temporal.append(cubo[2][2][2])

    cubo[2][2][0]=cubo[1][2][0]
    cubo[2][2][1]=cubo[1][2][1]
    cubo[2][2][2]=cubo[1][2][2]
    
    cubo[1][2][0]=cubo[5][0][2]
    cubo[1][2][1]=cubo[5][0][1]
    cubo[1][2][2]=cubo[5][0][0]
    
    cubo[5][0][2]=cubo[3][2][0]
    cubo[5][0][1]=cubo[3][2][1]
    cubo[5][0][0]=cubo[3][2][2]
    
    cubo[3][2][0]=lista_mov_temporal[0]
    cubo[3][2][1]=lista_mov_temporal[1]
    cubo[3][2][2]=lista_mov_temporal[2]
    
    rotacion_cara_derecha(4,cubo)
        
    #print cubo
    
def movimiento_u(cubo):

    lista_mov_temporal=copy.deepcopy(cubo[2][0])

    cubo[2][0][0]=cubo[1][0][0]
    cubo[2][0][1]=cubo[1][0][1]
    cubo[2][0][2]=cubo[1][0][2]
    
    cubo[1][0][0]=cubo[5][2][2]
    cubo[1][0][1]=cubo[5][2][1]
    cubo[1][0][2]=cubo[5][2][0]
    
    cubo[5][2][2]=cubo[3][0][0]
    cubo[5][2][1]=cubo[3][0][1]
    cubo[5][2][0]=cubo[3][0][2]
    
    cubo[3][0][0]=lista_mov_temporal[0]
    cubo[3][0][1]=lista_mov_temporal[1]
    cubo[3][0][2]=lista_mov_temporal[2]
    
    rotacion_cara_izquierda(0,cubo)
        
    #print cubo
    
def movimiento_U(cubo):
    
    lista_mov_temporal=copy.deepcopy(cubo[2][0])

    cubo[2][0][0]=cubo[3][0][0]
    cubo[2][0][1]=cubo[3][0][1]
    cubo[2][0][2]=cubo[3][0][2]
    
    cubo[3][0][0]=cubo[5][2][2]
    cubo[3][0][1]=cubo[5][2][1]
    cubo[3][0][2]=cubo[5][2][0]
    
    cubo[5][2][2]=cubo[1][0][0]
    cubo[5][2][1]=cubo[1][0][1]
    cubo[5][2][0]=cubo[1][0][2]
    
    cubo[1][0][0]=lista_mov_temporal[0]
    cubo[1][0][1]=lista_mov_temporal[1]
    cubo[1][0][2]=lista_mov_temporal[2]
    
    rotacion_cara_derecha(0,cubo)
        
    #print cubo
    
def movimiento_l(cubo):
    
    lista_mov_temporal = []
    lista_mov_temporal.append(cubo[0][0][2])
    lista_mov_temporal.append(cubo[0][1][2])
    lista_mov_temporal.append(cubo[0][2][2])

    cubo[0][0][2]=cubo[5][0][2]
    cubo[0][1][2]=cubo[5][1][2]
    cubo[0][2][2]=cubo[5][2][2]
    
    cubo[5][0][2]=cubo[4][0][2]
    cubo[5][1][2]=cubo[4][1][2]
    cubo[5][2][2]=cubo[4][2][2]
    
    cubo[4][0][2]=cubo[2][0][2]
    cubo[4][1][2]=cubo[2][1][2]
    cubo[4][2][2]=cubo[2][2][2]
    
    cubo[2][0][2]=lista_mov_temporal[0]
    cubo[2][1][2]=lista_mov_temporal[1]
    cubo[2][2][2]=lista_mov_temporal[2]
    
    rotacion_cara_izquierda(3,cubo)
        
    #print cubo
    
def movimiento_L(cubo):
    
    lista_mov_temporal = []
    lista_mov_temporal.append(cubo[0][0][2])
    lista_mov_temporal.append(cubo[0][1][2])
    lista_mov_temporal.append(cubo[0][2][2])

    cubo[0][0][2]=cubo[2][0][2]
    cubo[0][1][2]=cubo[2][1][2]
    cubo[0][2][2]=cubo[2][2][2]
    
    cubo[2][0][2]=cubo[4][0][2]
    cubo[2][1][2]=cubo[4][1][2]
    cubo[2][2][2]=cubo[4][2][2]
    
    cubo[4][0][2]=cubo[5][0][2]
    cubo[4][1][2]=cubo[5][1][2]
    cubo[4][2][2]=cubo[5][2][2]
    
    cubo[5][0][2]=lista_mov_temporal[0]
    cubo[5][1][2]=lista_mov_temporal[1]
    cubo[5][2][2]=lista_mov_temporal[2]
    
    rotacion_cara_derecha(3,cubo)
        
    #print cubo
    
def movimiento_r(cubo):
    lista_mov_temporal = []
    lista_mov_temporal.append(cubo[0][0][0])
    lista_mov_temporal.append(cubo[0][1][0])
    lista_mov_temporal.append(cubo[0][2][0])

    cubo[0][0][0]=cubo[2][0][0]
    cubo[0][1][0]=cubo[2][1][0]
    cubo[0][2][0]=cubo[2][2][0]
    
    cubo[2][0][0]=cubo[4][0][0]
    cubo[2][1][0]=cubo[4][1][0]
    cubo[2][2][0]=cubo[4][2][0]
    
    cubo[4][0][0]=cubo[5][0][0]
    cubo[4][1][0]=cubo[5][1][0]
    cubo[4][2][0]=cubo[5][2][0]
    
    cubo[5][0][0]=lista_mov_temporal[0]
    cubo[5][1][0]=lista_mov_temporal[1]
    cubo[5][2][0]=lista_mov_temporal[2]
    
    rotacion_cara_izquierda(1,cubo)
        
    #print cubo
    
def movimiento_R(cubo):
    
    lista_mov_temporal = []
    lista_mov_temporal.append(cubo[0][0][0])
    lista_mov_temporal.append(cubo[0][1][0])
    lista_mov_temporal.append(cubo[0][2][0])

    cubo[0][0][0]=cubo[5][0][0]
    cubo[0][1][0]=cubo[5][1][0]
    cubo[0][2][0]=cubo[5][2][0]
    
    cubo[5][0][0]=cubo[4][0][0]
    cubo[5][1][0]=cubo[4][1][0]
    cubo[5][2][0]=cubo[4][2][0]
    
    cubo[4][0][0]=cubo[2][0][0]
    cubo[4][1][0]=cubo[2][1][0]
    cubo[4][2][0]=cubo[2][2][0]
    
    cubo[2][0][0]=lista_mov_temporal[0]
    cubo[2][1][0]=lista_mov_temporal[1]
    cubo[2][2][0]=lista_mov_temporal[2]
    
    rotacion_cara_derecha(1,cubo)
        
    #print cubo

class Nodo:
    def __hash__(self):
        return int(self.hash)
    
    def __init__(self, script=None, padre=None, g=0):

        self.padre = padre
        self.script=script
        
        if(script==None):
            self.cubo = cubo_ordenado
            self.numero_cubetes_desordenados = 0
            self.h = 0
            self.f = 0
            self.g = 0
        else:    
            if self.padre == None:
                self.g = 0
                self.cubo=asignar_cubo(script,cubo_ordenado)
                self.numero_cubetes_desordenados=contar_cubetes_desordenados(self.cubo)
                
            else:            
                self.g = self.padre.g + 1
                self.cubo=asignar_cubo(script,padre.cubo)
            
            self.numero_cubetes_desordenados=contar_cubetes_desordenados(self.cubo)
            self.h = self.numero_cubetes_desordenados
            
            self.f = self.g + self.h
            self.hash = ""
            for cara in range(6):
                for fila in range(3):
                    for columna in range(3):
                        self.hash += str(self.cubo[cara][fila][columna])
    
    def gethijos(self):
        hijos = []
        movimientos="fFbBrRlLuUdD"
        if(self.padre == None):
            for i in range(len(movimientos)):
                hijos.append(Nodo(movimientos[int(i):int(i+1)], padre = self))
            return hijos
        else:            
            contrario = self.script.swapcase()
            for i in range(len(movimientos)):
                if(movimientos[int(i):int(i+1)] != contrario):
                    hijos.append(Nodo(movimientos[int(i):int(i+1)], padre = self))
            return hijos
    
    def __lt__(self, other):
        return self.f < other.f

    def __le__(self, other):
        return self.f <= other.f
        
    def __eq__(self, other):
        if(other == None):
            return False
        if(other.numero_cubetes_desordenados != self.numero_cubetes_desordenados):
            return False        
        if(obtener_cubete_1(self.cubo) != obtener_cubete_1(other.cubo)):
            return False
        if(obtener_cubete_2(self.cubo) != obtener_cubete_2(other.cubo)):
            return False
        if(obtener_cubete_3(self.cubo) != obtener_cubete_3(other.cubo)):
            return False
        if(obtener_cubete_3(self.cubo) != obtener_cubete_3(other.cubo)):
            return False
        if(obtener_cubete_4(self.cubo) != obtener_cubete_4(other.cubo)):
            return False
        if(obtener_cubete_5(self.cubo) != obtener_cubete_5(other.cubo)):
            return False
        if(obtener_cubete_6(self.cubo) != obtener_cubete_6(other.cubo)):
            return False
        if(obtener_cubete_7(self.cubo) != obtener_cubete_7(other.cubo)):
            return False
        if(obtener_cubete_8(self.cubo) != obtener_cubete_8(other.cubo)):
            return False
        if(obtener_cubete_9(self.cubo) != obtener_cubete_9(other.cubo)):
            return False
        if(obtener_cubete_10(self.cubo) != obtener_cubete_10(other.cubo)):
            return False
        if(obtener_cubete_11(self.cubo) != obtener_cubete_11(other.cubo)):
            return False
        if(obtener_cubete_12(self.cubo) != obtener_cubete_12(other.cubo)):
            return False
        if(obtener_cubete_13(self.cubo) != obtener_cubete_13(other.cubo)):
            return False
        if(obtener_cubete_14(self.cubo) != obtener_cubete_14(other.cubo)):
            return False
        if(obtener_cubete_15(self.cubo) != obtener_cubete_15(other.cubo)):
            return False
        if(obtener_cubete_16(self.cubo) != obtener_cubete_16(other.cubo)):
            return False
        if(obtener_cubete_17(self.cubo) != obtener_cubete_17(other.cubo)):
            return False
        if(obtener_cubete_18(self.cubo) != obtener_cubete_18(other.cubo)):
            return False
        if(obtener_cubete_19(self.cubo) != obtener_cubete_19(other.cubo)):
            return False
        if(obtener_cubete_20(self.cubo) != obtener_cubete_20(other.cubo)):
            return False
        
        return True
                    
    def __ne__(self, other):
        return not (self  == other)
    
    def __gt__(self, other):
        return self.f > other.f

    def __ge__(self, other):
        return self.f >= other.f
