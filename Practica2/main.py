"""
Created on Wed Oct 20 19:36:17 2021

@author: Diego Arellano
"""

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
    
  def get_raiz(self):
      return self.raiz  

    

#Definimos la clase del árbol de expresión
class Arbol_de_expresion(Arbol_binario):
    def __init__(self, dato, izq = None, der = None):
        self.raiz = Nodo(dato)
        self.izq = izq
        self.der = der
        if self.izq is not None: 
            self.raiz.set_hijo_izq(izq)
        if self.der is not None:
            self.raiz.set_hijo_der(der)
            
            
    def get_arbol_izq(self):
        return self.izq
    
    def get_arbol_der(self):
        return self.der
    
     
class Pila: 
    def __init__(self):
        self.pila = []
        
    def push(self, dato):
        self.pila.append(dato)
        
    def pop(self):
        if(not self.is_empty()):
            return self.pila.pop()
        return SystemError
        
    def is_empty(self): 
        return len(self.pila) == 0
        
    def peek(self):
        return self.pila[-1]
        
class Calculadora:
    
    def validar_operadores(self, expresion):
        tokens = expresion.split()
        i = 0
        if(self.es_operador(tokens[0]) or self.es_operador(tokens[-1])):
            return False
        while(i < len(tokens)-1):
            if(self.es_operador(tokens[i]) and self.es_operador(tokens[i+1])):
                return False
            else:
                i+= 1
        return True
    
    def validar_tokens(self, expresion): 
        tokens = expresion.split()
        for token in tokens:
            if(not self.es_operador(token) and not self.es_operando(token) and not token in ["(", ")"]):
                return False
        return True
            
    
    def validar_parentesis(self, expresion): 
        pila = Pila()
        tokens = expresion.split()
        for token in tokens:
            if(token == "("):
                pila.push(token)
            elif(token == ")"):
                if(not pila.is_empty()):
                    pila.pop()
                else:
                    return False
            
        return pila.is_empty()
    
    def es_operador(self, dato):
        return dato in ["+", "-", "*", "/"]
    
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
        if(not self.validar_tokens(expresion) or not self.validar_operadores(expresion) or not self.validar_parentesis(expresion)):
            return "Syntax ERROR"
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
            
        if(not pila_b.is_empty()):
            arbol = pila_b.pop()
        else:
            arbol = Arbol_de_expresion(0)
            
        return self.calcula(arbol)
        #print(arbol.get_arbol_izq().get_arbol_izq().get_arbol_der().get_raiz().get_dato())
        
    def calcula(self, arbol):
        if arbol.get_raiz().get_dato() == '+':
            return self.calcula(arbol.get_arbol_izq()) + self.calcula(arbol.get_arbol_der())
        elif arbol.get_raiz().get_dato() == '-':
            return self.calcula(arbol.get_arbol_izq()) - self.calcula(arbol.get_arbol_der())
        elif arbol.get_raiz().get_dato() == '*':
            return self.calcula(arbol.get_arbol_izq()) * self.calcula(arbol.get_arbol_der())
        elif arbol.get_raiz().get_dato() == '/':
            try:
                return self.calcula(arbol.get_arbol_izq()) / self.calcula(arbol.get_arbol_der())
            except ZeroDivisionError:
                return "Math ERROR"
        else:
            return arbol.get_raiz().get_dato()

calcu = Calculadora()
print(calcu.evaluar_expresion("3+2+1"))
print(calcu.evaluar_expresion("3 / 0"))
print(calcu.evaluar_expresion("3 + 3 * ( 2 - -1 )"))

''' No sé si la quieran poner pero se ve cool jsjasja
calcu = Calculadora()
print("Ingresa una expresión aritmética en notación infija")
print("Para terminar ingresa t")
print("Entre tokens debe haber un espacio")
expresion = input()
while(expresion != "t"):
    print(expresion + " = " + str(calcu.evaluar_expresion(expresion)))
    expresion = input()
'''