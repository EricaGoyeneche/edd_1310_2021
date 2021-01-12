def factorial(n):
    if n == 0:   #Si n es igual a cero
        return 1  #Entonces regresa 1
    else:          #De lo contrario o sea si no es cero
        return factorial(n-1)*n   #Entonces aplicar la formula

def printRev(n):  #EJEMPLO 2  Es un conteo regresivo
    if n > 0:  #Si n es mayor que cero
        #print(n)  #Entonces imprime n  ASI SALE 3,2,1
        printRev(n-1)  #Y printRev en su valor n-1
        print(n) #Asi sale 1,2,3

def fibonacci (n):  #EJEMPLO 3 fibonacci
    if n == 1 or n == 0: #Si n es igual a cero o uno
        return n    #Entonces regresa n
    if n > 1:    #Funciona para toda n-1
        return (fibonacci(n-1) + fibonacci (n-2))  #Aplicar la formnula


def main():
    for num in range(1,33,1):
       r = factorial(num)

       print(f"El factorial de {num} es {r}" )

def main3():
    for num in range(11):
     print(str(fibonacci(num)) +  "," , end="")
     print("")

def main2():
    printRev(3)




main3()
