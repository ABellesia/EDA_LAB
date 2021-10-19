
#Definimoss la clase nodo
class Nodo:
    def __init__(self, dato=None):
        self.dato = dato
        self.hijo_der = None
        self.datohijo_izq = None
        self.papa = None

    def set_hijo_der(self, dato):
        self.hijo_der = Nodo(dato)

    def set_hijo_izq(self, dato):
        self.hijo_izq = Nodo(dato)

    def get_dato():
        return self.dato

    def get_papa():
        return self.papa

    def set_papa(self, papa):
        self.papa = papa

    def get_hijo_der():
        return self.hijo_der

    def get_hijo_izq():
        return self.hijo_izq

class Arbol_binario:
  def __init__(self, dato = None):
      self.raiz = Nodo(dato)
      if dato == None: 
          self.cont = 0
      else: 
          self.cont = 1
  def size():
      return self.cont

#Definimos la clase del árbol de expresión
class Arbol_de_expresion(Arbol_binario):
    def __init__(self, dato, arbol_izq=None, arbol_der=None):
        self.raiz = Nodo(dato)
        if self.raiz.get_dato() == None:
            self.cont = 1
        else:
            self.cont = 0
        self.arbol_izq = arbol_izq
        self.arbol_der = arbol_der
        if arbol_der != None:
            self.count = self.count + arbol_der.size()
            self.raiz.set_hijo_der(arbol_der.get_raiz())
        if arbol_izq != None:
            self.count = self.count + arbol_izq.size()
            self.raiz.set_hijo_izq(arbol_izq.get_raiz())

    def get_raiz():
        return slef.raiz

    def evalua_arbol():
        return evalua_nodo(self.raiz)
        
    def evalua_nodo(self, raiz):
        if raiz == None: 
            res = 0
        else: 
            temp = raiz.get_dato()
            if es_Operador(temp) == True: 
                operando_1 = raiz.get_izq()
                operando_2 = raiz.get_der()
                res = calcula_termino(temp,operando_1, operando_2) 
            else:
                res = temp.get_Dato()
        return res
  def calcula_termino(operador, operando_1, operando_2):
      res = 0
      if operador == '+':
          res = operando_1 + operando_2
      elif operador == '-':
          res = operando_1 - operando_2
      elif operador == '*':
          res = operando_1 * operando_2
      else
          res = operando_1 / operando_2
      return res
  
  def es_Operador(dato):
      operadores = ['+','-','*','/']
      if dato in operadores:
          res = True
      else:
          res = False
      return res


class Pila(): 
    def __init__(self):
        self.pila = []
        
    def push(dato):
        self.pila.append(dato)
        
    def pop():
        self.pila.pop()
        
    def is_Empty(): 
        return len(self.pila) == 0
        
    def peek():
        return self.pila[-1]
        
class Calculadora:
  def __init__(self, expresion):
    self.expresion = expresion

  def post_fija(expresion):
      return expresion_post_fija

  def es_Operador(dato):
      operadores = ['+','-','*','/']
      if dato in operadores:
          res = True
      else:
          res = False
      return res

  def es_Operando(dato): 
    try:
      float(dato)
      return True
    except ValueError:
      return False
  
  def evaluar_expresion(): 
    pila_a = Pila()
    pila_b = Pila()
    tokens = self.expresion.split()
    while len(tokens) != 0:
      token = tokens.pop(0)
      if es_Operando(token) 
        pila_b.push(Arbol_de_expresion(float(token))
      elif token == "(":
        pila_a.push(token)
      elif token == "(":
        

      
        
    