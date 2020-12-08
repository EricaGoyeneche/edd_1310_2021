from backtracking import LaberintoADT
import time
pasillos_inicial = ((2,1),(2,2),(2,3),(2,4),(3,2),(4,2))
lab = LaberintoADT(6,6,pasillo_inicial, (5,2),(2,5))
lab.buscar_entrada()
lab.to_string()
lab.imprimir_camino()

while not lab.es_salida(lab.get_pos_actual()[0], lab.get_pos_actual()[1]):  #Siempre que sea necesario se aplicarán las 6 regls
    print('Probar')
    lab.resolver_laberinto()
    lab.imprimir_camino()
     time.sleep(1.0)
