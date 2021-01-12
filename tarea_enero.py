def suma_lista_rec(lista):
    if len(lista) ==1:   #Si la longitud de la lista es 1
        return lista[0]   #Entonces regresa 0
    else:     #De lo contrario
        return lista.pop() + suma_lista_rec(lista)   #Va a quitar el último elemento y agregara la lista 

def main():
    datos = [4,2,3,5]
    res = suma_lista_rec(datos)
    print(res)


main()
