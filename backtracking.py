from Array2D import Array2D
class LaberintoADT:
    """
    0 - pasillo SERÁ UNA TUPLA
    1- pared
    2 - salida
    e - entrada SERÁ EN UNA TUPLA
    """
    def __init__(self, rens, cols, pasillos, entrada, salida):
        self.__laberinto = Array2D(rens, cols, '1')
        for pasillo in pasillos:
            self.__laberinto.set_item(pasillo[0],pasillo[1],'0')
        self.set_entrada(entrada[0],entrada[1])
        self.set_salida(salida[0],salida[1])
        self.__camino = Stack()
        self.__previe = None

    def to_string(self):
        self.__laberinto.to_string()

    def set_entrada(self, ren, col):
       #Terminar la validación de las coordenadas TAREA
        self.__laberinto.set_item(ren,col,'E')

    def set_salida(self, ren, col):
       #TAREA TERMINAR LAS VALIDACIONES
        self.__laberinto.set_item(ren,col,'S')

    def es_salida(self, ren, col):
        return self.__laberinto.get_item(ren,col) == 'S'

    def buscar_entrada(self):
        encontrado = False
        for renglon in range(self.__laberinto.get_num_rows()):
            for columna range(self.__laberinto.get_num_cols()):
               tope = self.__camino.peek() #Va a regresar una tupla
               if self.__laberinto.get_item(renglon, columna) == 'E'
                  self.__camino.push((renglon,columna))
                  encontrado = True
        return encontrado

    def set_previa( self, pos_previa):
        self.__previa = pos_previa

    def get_previa(self):
        return self.__previa

    def imprimir_camino(self):
        self.__camino.to_string()

    def imprimir_pila(self):
        self.__camino.to_string()

    def get_pos_actual(self):
        return self.__camino.peek()

    def resolver_laberinto(self):
        actual = self.__camino.peek()  #5,2

        #Regla 1 BUSCAR A LA IZQUIERDA      pos actual es 5,2
        #Se le resta uno porque es la de la izquierda y preguntamos si es 0 o sea si hay pasillo
        if actual[1]-1 != -1\
         and self.__laberinto.get_item(actual[0],actual[1]-1) =='0' \
         and self.get_previa() != (actual[0],actual[1]-1) \  #Regla 6 va implicita en todas
         and self.__laberinto.get_item(actual[0],actual[1]-1) != 'X':
             self.set_previa(actual)
             self.__camino.push(actual[0],actual[1]-1)

        #REGLA 2 BUSCAR ARRIBA
        elif actual[0]-1 != -1\
         and self.__laberinto.get_item(actual[0]-1,actual[1]) =='0' \
         and self.get_previa() != (actual[0]-1,actual[1]) \  #Regla 6 va implicita en todas
         and self.__laberinto.get_item(actual[0]-1,actual[1]) != 'X':
             self.set_previa(actual)
             self.__camino.push((actual[0]-1,actual[1]))

        #REGLA 3 BUSCAR DERECHA
        elif 1==0:
          pass



        #REGLA 4 BUSCAR ABAJO
        elif 1==0:
            pass
        else:
            self.__laberinto.set_item(actual[0],actual[1], 'X')
            self.__previa = actual 
            self.__camino.pop()  #Con esto hacemos backtracking
