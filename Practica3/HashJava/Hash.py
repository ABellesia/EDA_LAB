class Film:
    def __init__(self, title, date, rate):
        self.title = title
        self.date = date 
        self.rate = rate
    def to_String(self):
        return "Film{"+"title= "+self.title+", date= "+self.date+", rate="+self.rate+"}"
    def get_Title(self):
        return self.title
    
class NodoHash:
    def __init__(self, dato):
        self.dato = dato
    def set_Sig(self, sig):
        self.sig = sig
    def get_Dato(self):
        return self.dato
    def get_sig(self):
        return self.sig
    
class HashTable:
    def __init__(self, m):
        self.cont = 0
        self.arreglo = []
        for i in range(0,m):
            self.arreglo.append(NodoHash(None))
        self.m = m
    def insertar(self, elem):
        nodo = NodoHash(elem)
        self.cont += 1
        pos = abs(elem.get_Title().hash % self.m)
        sig = self.arreglo[pos].get_sig()
        self.arreglo[pos].set_Sig(nodo)
        nodo.set_Sig(sig)
        
    def expande(self):
        arregloNuevo = []
        n = len(self.arreglo)*2
        for i in range(0,n):
            arregloNuevo.append(NodoHash(None))
        for i in range(0,len(self.arreglo)):
            actual = self.arreglo[i].get_sig()
            while actual != None:
                pos = actual.get_Dato().hash % len(arregloNuevo)
                nuevo = NodoHash(actual.get_Dato())
                sig = arregloNuevo[pos].get_sig()
                arregloNuevo[pos].set_Sig(nuevo)
                nuevo.set_Sig(sig)
                actual = actual.get_sig()
        self.arreglo = arregloNuevo
        
    def find(self, elem):
         pos = abs(elem.get_Title().hash % self.m)
         actual = self.arreglo[pos]
         while actual.get_sig() != None and actual.get_sig().get_Dato().get_Title != elem:
             actual = actual.get_sig()
         if actual.get_sig() != None and actual.get_sig().get_Dato().get_Title == elem:
             return actual
         else:
             return None 
         
    def eliminar(self, elem):
        ant = self.find(elem)
        if ant == None:
            return None
        self.cont -= 1
        target = ant.get_sig()
        sig = target.get_sig()
        target.set_Sig(None)
        ant.set_Sig(sig)
        return target
    
    def to_String(self):
        cad = ""
        for i in range(0,len(self.arreglo)):
            actual = self.arreglo[i]
            while actual != None: 
                if actual.get_Dato() == None:
                    cad = cad + "c "
                else: 
                    cad = cad + actual.get_Dato()+","
                actual = actual.get_sig()
            cad = cad + "\n"
        return cad
    
    def get_cont(self):
        return self.cont
    
    
    
lista = []
file = open("imbd.csv", "r")
contenido = file.read()
aux = contenido.split('\n')
for i in contenido:
    aux2 = i.split(',')
    lista.append(Film(aux2[0], aux2[1], aux2[2]))
hashy = HashTable(5)
for i in range(len(lista)):
    hashy.insertar(lista[i])
print(hashy.to_String())


