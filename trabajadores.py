from arrays import arrays   #Importando desde ADT que hicimos en la clase 
#Ejecutar en la consola pruebas.py

junio = '/content/junio1.txt'   #Abrir el archivo
with open (junio) as f_obj:
 trabajador = f_obj.readlines()
for line in lines:
 print(line)

lista = len(trabajador)
trabajador = Array(lista)
aumento =  float(276.5)       #Debe ser float por decimales

for x in range(1,lista):
  trabajador.set_item(trabajador[x],x)

print('DATOS DE TRABAJADORES')
for x in range (1,lista):
   extra = int(trabajador.get_item(x)[4])
   ingreso = int(trabajador._get_item(x)[6])
   sueldo = int(trabajador.get_item(x)[5])
   pago_extra = sueldo + (extra * aumento)
   antiguedad = (2020 - ingreso) * 0.03
   pago_total = float((sueldo*antiguedad)+extra)

print(f'Cédula de trabajador:{trabajador[x][0]} Trabajador:{trabajador[x][1]} {trabajador[x][2]} {trabajador[x][3]} Sueldo: ${pago_total}')
print('---- BONO DE ANTIGÜEDAD ---')

for x in range(1,lista):
  if int(trabajador.get_item(x)[6])==2016:
         print(f'El bono del trabajador más antigüo es para:{trabajador[x][1]}{trabajador[x][2]} {trabajador[x][3]} Por haber ingresado en el año:{trabajador[x][6]}')

print('--- TRABAJADOR CON MENOS AÑOS EN LA EMPRESA ---')

for x in range(1,lista):
  if int(trabajador.get_item(x)[6])==2020:
         print(f'Trabajador sin bono por menos años en la empresa:{trabajador[x][1]}{trabajador[x][2]} {trabajador[x][3]} Por haber ingresado en el año:{trabajador[x][6]}')
