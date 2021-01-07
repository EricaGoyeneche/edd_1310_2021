from colas import Queue, BoundedPriorityQueue

q1 = Queue()
q1.enqueue(3)
q1.enqueue(33)
q1.enqueue(23)
print(q1.to_string())

print("Prueba 2 de Queue")
c1 = {"id":1, "nombre":"Mario", "balance": 20.5}
c2 = {"id":2, "nombre":"Diana", "balance": 3456.5}
c3 = {"id":3, "nombre":"Bartolo", "balance": 1000000.0}

atencion = Queue()
atencion.enqueue(c1)
atencion.enqueue(c2)
atencion.enqueue(c3)

print(atencion.to_string())
siguiente= atencion.dequeue()
print(f" Bienvenido Sr. {Siguiente['Nombre']}, en qué podemos ayudarle?")


print("PRUEBAS DE LAS COLAS CON PRIORIDAD ACOTADA")

maestres = {"Prioridad": 4 , "Descripcion": "Maestres" , "Personas": ["Juan p" , "Diego H"]}
niños = {"Prioridad": 2 , "Descripcion": "Niños" , "Personas": ["Santi H" , "Angel H"]}
mecanicos = {"Prioridad": 4 , "Descripcion": "Mecanicos" , "Personas": ["Diana T" , "Maria Z"]}

cpa = BoundedPriorityQueue(7)
cpa.enqueue(maestres['Prioridad'], maestres) #Requiere dos argumentos
cpa.enqueue(niños['Prioridad'], niños)
cpa.enqueue(mecanicos ['Prioridad'], mecanicos)
cpa.to_string()
sig.cta.dequeue()
print(sig)
