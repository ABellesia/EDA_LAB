import numpy as np
import csv

class Nodo_Hash:
	def __init__(self, dato = None):
		self.dato = dato
		self.siguiente
	
	def get_dato(self):
		return self.dato
	
	def get_siguiente(self):
		return self.siguiente

	def set_siguiente(self, nodo):
		self.siguiente = nodo

class Tabla_Hash:
	def __init__(self, m):
		self.cont = 0
		self.m = m  
		self.arre = np.array([None for i in range(m)])
		self.arre[0] = None
		self.factor_carga = 0.8


	def inserta(self, dato):
		nodo = Nodo_Hash(dato)
		self.cont += 1
		if (self.cont/len(self.arre)) > self.factor_carga:
			self.expande()
		pos = dato.hashCode() % len(self.arre)
		sig = self.arre[pos].get_siguiente()
		self.arre[sig].set_siguiente(nodo)
		nodo.set_siguiente(sig)

	def find(self, elem):
		pos = elem.hashCode() % len(self.arre)
		actual = self.arre[pos]
		while (actual.get_siguiente() != None and actual.get_siguiete().get_dato() == elem):
			actual = actual.get_siguiente()
		if (actual.get_siguiente() != None and actual.get_siguiete().get_dato() == elem):
			return actual
		return None

class Film:
    
    def __init__(self, title, date, rate):
        self.title = title
        self.date = date
        self.rate = rate
    def __str__(self):
        return self.title


list = []

with open('imdb.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter = ',')
        line_count=0
        for row in csv_reader:
            if line_count != 0:
                list.append(Film(row[0],row[1],row[2]))
            line_count += 1

for x in range(len(list)):
    print(list[x])
print(len(list))	

