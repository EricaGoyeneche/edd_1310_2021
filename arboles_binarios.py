class NodoArbol:    #ESTE ES EL NODO ARBOL ES EL PRINCIPAL
    def __init__(self, value, left=None, right=None): #Hijo derecho e hijo izquierdo
        self.data = value
        self.left = left
        self.right = right

class BinarySearchTree:  #Arbol binario de busqueda
    def __init__(self):
        self.__root = None #Es una rama vacía

    def insert(self, value):
        #regla 1
        if self.__root == None:  #Esto es lo mismo #self.__root is None
             self.__root = NodoArbol(value, None, None)
        #Si no está vcío se aplica la regla 2
        else:
            self.__insert__(self.__root, value)

    def __insert__(self, nodo, value):  #El nodo es una copia de la raíz
       if nodo.data == value:  #Preguntar si el nodo es igual al valor
           print("El dato ya existe, no se ingresa nada")
       elif value < nodo.data:    #Preguntar si es menos que el nodo.data o sea el valor anterior
         #REGLA 1 OTRA VEZ
          if nodo.left == None:   #Si el nodo izquiero esta vacío
             nodo.left = NodoArbol(value)  #Checar el valor del nodo
          #REGLA 2 OTRA VEZ
          else:
            self.__insert__(nodo.left, value)   #Entonces insertar el valor que estamos recibiendo
       else:
        if nodo.right == None:              #Ahora del lado derecho
            nodo.right = NodoArbol(value)
        else:
             self.__insert__(nodo.right, value)

    def __recorrido_in(self, nodo):
        if nodo != None:  #Mientras el nodo sea diferente de None, o sea que no lleguemos a uno vacio entonces aplica recursividad
            self.__recorrido_in(nodo.left)
            print(nodo.data, end=" , ")
            self.__recorrido_in(nodo.right)

    def __recorrido_pos( self, nodo ):
        if nodo:
            self.__recorrido_pos(nodo.left)
            self.__recorrido_pos(nodo.right)
            print(nodo.data, end=", ")


    def __recorrido_pre( self, nodo ):
        if nodo:
            print(nodo.data, end=", ")
            self.__recorrido_pre(nodo.left)
            self.__recorrido_pre(nodo.right)

    def transversal(self, format='inorden'):
        if format == 'inorden':
            self.__recorrido_in(self.__root)
        elif format == 'Preorden':
            print('Recorrido en pre')
            self.__recorrido_pre(self.__root)
        elif format == 'Posorden':
            print('Posorden')
            self.__recorrido_pos(self.__root)
        else:
            print('Error, ese formato no existe')
        print("")

    def search(self, value):
       if self.__root == None:
           return None
       else:
           return self.__search(self.__root, value)

    def __search(self, nodo, value):
       if nodo == None:  #Está vacío???
           print('Caso Base')
           return None
       elif nodo.data == value: #Caso base de recursividad
           print("Encontrado")
           return nodo
       elif value < nodo.data:
           print('Buscar a la  izquierda')
           return self.__search(nodo.left, value)
       else:
           print('Buscar a la derecha')
           return self.__reach(nodo.right, value)

    def remove(self, value):
         #caso 1
         if encontrado.left == None and encontrado.right == None:  #Significa que es un nodo hoja
            encontrado = None
         #caso 2
         elif (encontrado.left != None  and encontrado.right == None) or (encontrado.left == None  and encontrado.right != None): #Del lado derecho hay algo y del izquierodo no
              print("A eliminar:", encontado.data)
