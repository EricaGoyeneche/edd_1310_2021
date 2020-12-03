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
                  self.__camino.push(tuple(renglon,columna))
                  encontrado = True
        return encontrado

    def set_previa( self, pos_previa):
        self.__previa = pos_previa

    def get_previa(self):
        return self.__previa

   def resolver_laberinto(self):
#COMENZAR A RESOLVER
