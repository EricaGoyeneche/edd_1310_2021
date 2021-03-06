class Queue:
  def __init__(self):
    self.__data = list() #[constructor]

  def is_empty(self):
    return len(self.__data) == 0

  def lenght( self ):
    return len(self.__data)

  def enqueue(self, elem):
    self.__data.append(elem)

  def dequeue ( self ):
    if not self.is_empty():
      return self.__data.pop(0)
    else:
      return None

  def to_string(self):
    cadena = ""
    for elem in self.__data:
      cadena = cadena + "|" + str(elem)
    cadena = cadena + "|"
    return cadenas

#TAREA PriorityQueue



class BoundedPriorityQueue:
    def __init__(self, niveles):
        self.__data = [ Queue() for x in range(niveles)] #Arreglo privado de tipo lista Es una lista pyhton en donde en cada nivel hay una cola vacía
        self.__size = 0

    def is_empty(self):
        return self.__size == 0

    def lenght (self):
        return self.__size

    def enqueue(self, prioridad, elem):  #poner
        if prioridad < len(self.__data) and prioridad >= 0:  #Si se cumple esta condición entonces si se puede agregar un valor
            self.__data[prioridad].enqueue(elem)
            self.__size += 1

    def dequeue(self):  #sacar datos
    if not self.is_empty():
      for nivel in self.__data:
            if not nivel.is_empty():
                self.__size -=1
                return nivel.dequeue()

    def to_string(self):
        print("cola:")
        for nivel in range(len(self.__data)):
            print(f"Nivel {nivel} --> {self.__data[nivel].to_string()}")
