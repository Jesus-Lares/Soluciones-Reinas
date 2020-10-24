import numpy as np

def insertarReinas(reinas,reina,NoReina):
    soluciones={}
    while reinas[0] != NoReina :
        retroceso=True
        #Buscara una posicion disponible para la reina en movimiento
        for i in range(NoReina):
            if(i not in reinas and validarReinas(reinas,reina,i) and reinas[reina]<i): 
                reinas[reina]=i
                reina+=1
                print("\tposiciones actuales ",reinas,"\tnumero de reina en movimiento",reina,"\tposicion ",i) 
                retroceso=False
                break
        
        if(retroceso):
            #Entrara cuando se complete una solucion y retrocedera para buscar otra
            if reina==NoReina:
                soluciones[str(len(soluciones))]=reinas
                print("\nSe agrego solucion:",reinas,"\n" )
                reinas[reina-1]=-1
                reina-=2

            #Terminara el ciclo al completar todas las opciones posibles a seguir
            elif reina==0:
                reinas[reina]+=1
                print("\nSe acabo la busqueda de soluciones")
            
            #Al no encontrar una posicion disponible regresara la posicion de la reina e intentara con otra posicion
            else:
                print("retroceso a reina:",reina-1 )
                reinas[reina]=-1
                reina-=1

    return soluciones
            
def validarReinas(reinas,reina,posicion):
    if(reina==0):
        return True
    else:
        retorno = 0
        for i in range(reina):
            descuento=1+i
            if(reinas[reina-descuento]+descuento!=posicion and reinas[reina-descuento]-descuento!=posicion ):
                retorno+=1
        return retorno==reina
    return False

def puestas(n,reinas,reina):
    matriz=np.zeros((n, n))
    for i in range(reina):
        matriz[reinas[i]][i]=1
    print(matriz)


NoReina=int(input("insertar el numero de reinas: "))
reinas=[]
for i in range(NoReina):
    reinas.append(-1)

soluciones=insertarReinas(reinas,0,NoReina)
print("Numero de soluciones: ",len(soluciones))