#logica con python
'''
edad=int(input("digita tu edad: "))
print(edad)

#condicion logica simple
bandera=True
if(edad>=18 or bandera==True):
    print("Bienvenido a la chismosa")

else:
    print("Devolvete por favor")

#Ejemplo 1 Hidroituango
nivelAgua=float(input("Digita el nivel del agua: "))

if(nivelAgua>0 and nivelAgua<200):
    print("La represa tiene poca agua")
elif(nivelAgua>=200 and nivelAgua<450):
    print("La represa esta ok")
elif(nivelAgua>=450):
    print("PELIGRO, abra las compuertas")
else:
    print("Digito un nivel invalido")


#Ejemplo 2 Estaciones del año



mes=input("Digite el mes del año que desea consultar: ").lower()


if(mes=='enero' or mes=='febrero' or mes=='marzo'):
    print("El mes digitado pertenece a la estacion Invierno")
elif(mes=='abril' or mes=='mayo' or mes=='junio'):
    print("El mes digitado pertenece a la estacion verano")
elif(mes=='julio' or mes=='agosto' or mes=='septiembre'):
    print("El mes digitado pertenece a la estacion otoño")
elif(mes=='octubre' or mes=='noviembre' or mes=='diciembre'):
    print("El mes digitado pertenece a la estacion Primavera")
else:
    print("Error al digitar")
'''

#ejemplo 3 edades
edad=float(input("digita tu edad: "))

if(edad>0 and edad<=14):
    print("La estapa de la vida en la que se enceuntra es: NIÑO ")
elif(edad>14 and edad<=28):
    print("La estapa de la vida en la que se enceuntra es: JOVEN ")
elif(edad>28 and edad<60):
    print("La estapa de la vida en la que se enceuntra es: ADULTO ")
elif(edad>=60):
    print("La estapa de la vida en la que se enceuntra es: ADULTO MAYOR ")
else:
    print("Error al digitar")

#ejemplo 4 operador ternario
parametro=True
print("el parametro es verdadero")if parametro==True else print("el parametro es falso")


