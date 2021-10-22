# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 19:36:17 2021

@author: Diego Arellano
"""

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
      if nodo != None:
          self.post_orden(nodo.hijo_izq)
          self.post_orden(nodo.hijo_der)
          print(nodo.get_dato())

    

#Definimos la clase del árbol de expresión
class Arbol_de_expresion(Arbol_binario):
    def __init__(self, dato, arbol_izq=None, arbol_der=None):
        self.raiz = Nodo(dato)
        if self.raiz.get_dato() == None:
            self.cont = 1
        else:
            self.cont = 0
        self.raiz.set_hijo_izq(arbol_izq)
        self.raiz.set_hijo_der(arbol_der)
        if arbol_der != None:
            self.cont = self.cont + arbol_der.size()
            self.raiz.set_hijo_der(arbol_der.get_raiz())
        if arbol_izq != None:
            self.cont = self.cont + arbol_izq.size()
            self.raiz.set_hijo_izq(arbol_izq.get_raiz())




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
                pila_b.push(Arbol_de_expresion(float(token)))
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
        arbol.post_ordenR()


calcu = Calculadora()
calcu.evaluar_expresion(" 2 * 6  / 3 * 5")


