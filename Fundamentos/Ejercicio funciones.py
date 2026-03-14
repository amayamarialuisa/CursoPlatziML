#Ejercicio 1

def saludar (nombre):
    print("Hola,", nombre,"!")

saludar("Maria")

#Ejercicio 2

def cuadrado (numero):
    print(f"El cuadrado de {numero} es: {numero**2}")

cuadrado(4)

#Ejercicio 3

def es_par(numero_2):
   return numero_2 % 2 == 0
print(es_par(2))
print(es_par(3))

#Ejercicio 4

def mayor(a, b):
    return a if a > b else b
print(mayor(2, 1))

#Ejercicio 5

def calcular_area_rectangulo(base, altura):
    return base * altura
print(calcular_area_rectangulo(4, 5))

#Ejercicio 6

def convertir_celsius_a_fahrenheit(celsius):
    return (celsius * 9) / 5 + 32
print(convertir_celsius_a_fahrenheit(4))

#Ejercicio 7

def suma_lista(lista):
    return sum(lista)
print(suma_lista([3,4,7,9,10,17]))

#Ejercicio 8

def numero_mayor_lista(lista):
    return max(lista)
print(numero_mayor_lista([1,5,7,88]))

#Ejercicio 9

def contar_pares(lista):
    contador = 0
    for numero in lista:
        if numero % 2 == 0:
            contador += 1
    return contador
print(contar_pares([1,2,3,4,5,6]))

#Ejercicio 10

def promedio(lista):
    return (sum(lista) / len(lista))

print(promedio([10,20,30,40]))

#Ejercicio 11

def numero_mayor(lista):
    return max(lista)
print(numero_mayor([3,7,2,9,5]))

#Ejercicio 12
def numero_menor(lista):
    return min(lista)

print(numero_menor([8,4,10,2,7]))

#Ejercicio 13

def contar_mayores(lista, limite):
    contador = 0
    for numeros in lista:
        if numeros > limite:
            contador += 1
    return contador
print(contar_mayores([10,25,30,5,8], 20))

#Ejercicio 14

def contar_pares(lista):
    contador = 0
    for numero in lista:
        if numero % 2 == 0:
            contador += 1
    return contador
print(contar_pares([1,2,3,4,5,6]))

#Ejercicio 15

def suma_mayores(lista, limite):
    suma = 0
    for numeros in lista:
        if numeros > limite:
            suma += numeros
    return suma
print(suma_mayores([5,12,7,20,3],10))

#Ejercicio 16

def contar_negativos(lista):
    contador = 0
    for numeros in lista:
        if numeros < 0:
            contador += 1
    return contador
print(contar_negativos([3,-2,5,-8,1]))

#Ejercicio 17

def duplicar(lista):
    nueva_lista = []
    for numeros in lista:
        nueva_lista.append(numeros * 2)
    return nueva_lista
print(duplicar([1,2,3,4]))

print("----------------------------")
print("Repaso")

print("Ejercicio 1")

def num_mayores(lista, limite):
    contador = 0
    for numero in lista:
        if numero > limite:
            contador += 1
    return contador
print(num_mayores([5,12,8,20,3], 10))

print("Ejercicio 2")

def cuadrados(lista):
    nueva_lista = []
    for numero in lista:
        nueva_lista.append(numero**2)
    return nueva_lista
print(cuadrados([1,2,3,4]))

print("Ejercicio 3")

def suma_pares(lista):
    suma = 0
    for numero in lista:
        if numero % 2 == 0:
            suma += numero
    return suma
print(suma_pares([1,2,3,4,5,6]))

print("Ejercicio 4")

def menor_negativo(lista):
    negativos = []
    for numero in lista:
        if numero < 0:
            negativos.append(numero)
    return min(negativos)
print(menor_negativo([3,-2,-7,5,-1]))

print("Ejercicio 5")

def solo_pares(lista):
    nueva_lista = []
    for numero in lista:
        if numero % 2 == 0:
            nueva_lista.append(numero)
    return nueva_lista
print(solo_pares([1,2,3,4,5,6,7]))


def duplicar(lista):
    return [numero for numero in lista if numero*2 ]
print(duplicar([1,2,3,4]))

