'''
Created on 29/04/2010

@author: lporras
'''
from _heapq import heappush, heappop, heapify
from nodo import Nodo


class Aestrella:

    def start(self, script):
        self.inicio = Nodo(script)
        self.final = Nodo()
        lista_abierta = []
        lista_cerrada = {}
        
        heappush(lista_abierta, self.inicio)

        while(lista_abierta):

            nodo_actual = heappop(lista_abierta)
            while(nodo_actual.g > len(script)):
                nodo_actual = heappop(lista_abierta)

            if(nodo_actual == self.final):
                print "Solucion Encontrada"
                self.lista_cerrada = lista_cerrada
                print 'Estados recorridos: '+str(len(lista_cerrada))
                print 'Estados a visitar: '+str(len(lista_abierta))
                print 'g: '+str(nodo_actual.g)
                print 'h: '+str(nodo_actual.h)
                return self.devolverRuta(nodo_actual)
            
            lista_cerrada[nodo_actual] = 'eliminado'
            
            for y in nodo_actual.gethijos():
                if(not y in lista_cerrada):
                    
                    if(y.g <= len(script)):
                        a = self.seek(lista_abierta,y)
                        if (a == None):
                            heappush(lista_abierta,y)
                        elif(nodo_actual.g + 1 < y.g):
                            a.g = y.g
                            a.h = y.h
                            a.f = y.f
                            a.padre = y.padre
                            a.script = y.script
                            heapify(lista_abierta)
        return "Ha ocurrido un Error"
    
    
    def seek(self, theset, c):
        try:
            return theset[theset.index(c)]
        except ValueError:
            return None
    
    def devolverRuta(self, estado_actual):
        if(estado_actual.padre != None):
            return self.devolverRuta(estado_actual.padre) + estado_actual.script
        else:
            return " "
   
    

    

    
    
