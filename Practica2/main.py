# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 19:36:17 2021

@author: Diego Arellano
"""

#Definimos la clase nodo
#Definimos la clase nodo
class Nodo:
    def __init__(self, dato=None):
        self.dato = dato
        self.hijo_der = None
        self.hijo_izq = None
        self.papa = None

    def set_hijo_der(self, dato):
        self.hijo_der = Nodo(dato)

    def set_hijo_izq(self, dato):
        self.hijo_izq = Nodo(dato)

    def get_dato(self):
        return self.dato

    def get_papa(self):
        return self.papa

    def set_papa(self, papa):
        self.papa = papa

    def get_hijo_der(self):
        return self.hijo_der

    def get_hijo_izq(self):
        return self.hijo_izq
    
    def __str__(self):
        cad = "" + str(self.dato)
        return cad

class Arbol_binario:
  def __init__(self, dato = None):
      self.raiz = Nodo(dato)
      if dato == None: 
          self.cont = 0
      else: 
          self.cont = 1
    
    
  def size(self):
      return self.cont
  
  def get_raiz(self):
      return self.raiz  

  def post_ordenR(self):
      self.post_orden(self.get_raiz())
      
  def post_orden(self, nodo):
      if nodo:
          self.post_orden(nodo.hijo_izq)
          self.post_orden(nodo.hijo_der)
          print(nodo.get_dato())

    

#Definimos la clase del árbol de expresión
class Arbol_de_expresion:
    def __init__(self, dato, izq, der):
        self.raiz = Nodo(dato)
        self.izq = izq
        self.der = der
        if self.izq is not None: 
            self.raiz.set_hijo_izq(izq)
        if self.der is not None:
            self.raiz.set_hijo_der(der)
            
    def get_raiz(self):
        return self.raiz  
        
    def get_arbol_izq(self):
        return self.izq
    
    def get_arbol_der(self):
        return self.der
    
    def post_ordenR(self):
        self.post_orden(self.raiz)
      
    def post_orden(self, nodo):
        if nodo is not None:
            self.post_orden(nodo.get_hijo_izq())
            self.post_orden(nodo.get_hijo_der())
            print(nodo)
            


class Pila: 
    def __init__(self):
        self.pila = []
        
    def push(self, dato):
        self.pila.append(dato)
        
    def pop(self):
        return self.pila.pop()
        
    def is_empty(self): 
        return len(self.pila) == 0
        
    def peek(self):
        return self.pila[-1]
        
class Calculadora:
    
    def es_operando(self, dato): 
        try:
            float(dato)
            return True
        except ValueError:
            return False
  
    def jerarquia(self, signo):
      if signo == "+" or signo == "-" :
          return 1
      elif signo == "*" or signo == "/":
          return 2
      return 0
  
    def crear_arbol(self, pila_a, pila_b):
        der = pila_b.pop()
        izq = pila_b.pop()
        pila_b.push(Arbol_de_expresion(pila_a.pop(), izq, der))


    def evaluar_expresion(self, expresion): 
        pila_a = Pila()
        pila_b = Pila()
        tokens = expresion.split()
        while len(tokens) > 0:
            token = tokens.pop(0)
            if self.es_operando(token):
                pila_b.push(Arbol_de_expresion(float(token), None, None))
            elif token == "(" :
                pila_a.push(token)
            elif token == ")" :
                while(pila_a.peek() != "("):
                    self.crear_arbol(pila_a, pila_b)
                pila_a.pop()
            else: 
                while(not pila_a.is_empty() and pila_a.peek() != "(" and self.jerarquia(pila_a.peek()) >= self.jerarquia(token)):
                    self.crear_arbol(pila_a, pila_b)
                pila_a.push(token)
                    
        while(not pila_a.is_empty()):
            self.crear_arbol(pila_a, pila_b)

        arbol = pila_b.pop()
        #print(arbol.get_arbol_izq().get_arbol_izq().get_arbol_der().get_raiz().get_dato())


calcu = Calculadora()
calcu.evaluar_expresion("( 2 - 6 ) * 3 + 5")


