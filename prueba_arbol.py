class NodoArbol:    #ESTE ES EL NODO ARBOL ES EL PRINCIPAL
    def __init__(self, value, left=None, right=None): #Hijo derecho e hijo izquierdo
        self.data = value
        self.left = left
        self.right = right
arbol = NodoArbol("R", NodoArbol("C"),NodoArbol("H"))
print(arbol.left.data)
print(arbol.data)
print(arbol.right.data)

arbol2 = NodoArbol(4, NodoArbol(3, NodoArbol(2, NodoArbol(2))), NodoArbol(5)) #Ejemplo 2
print(arbol2.data)
print(arbol2.left.data)
print(arbol2.right.data)
print(arbol2.left.left.data)
print(arbol2.left.left.left.data)
