class Stack:
    def __init__(self):
        self.__data = list()

    def is_empty(self): #Está vacio?
        return len(self.__data) == 0

    def lenght(self): #Longitud de elementos que almacena
        return

    def pop(self):      #Para sacar valores, se pone el if por si ya no hay más tambien se puede con un try catch
        if self.is_empty():
            print('Pila vacía')
        else:
        return self.__data.pop()

    def push(self, value):
        self.__data.append(value)

    def peek(self):  #Saca el valor que está al final
       return self.__data[len(self.__data)-1]

    def to_string(self):  #Saber el estado actual de las pilas
          print("-------")
       for item in self.__data[::-1]:
           print(f"|{item}|")
           print("-------")
