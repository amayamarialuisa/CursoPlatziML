class Person:
    def __init__(self, name, age):
        self.name = name
        self. age = age
    def greet(self):
        print(f"Hola, mi nombre es {self.name} y tengo {self.age}")

person1 = Person("Ana",30)
person2 = Person("Luis", 25)

person1.greet()
person2.greet()

##Ejercicio 1

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f"Hola, soy {self.nombre} y tengo {self.edad} años")

p = Persona("Carlos", 25)
p.saludar()

##Ejercicio 2

class Rectangulo:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    def area(self):
        return self.ancho * self.alto

    def perimetro(self):
        return 2 * (self.ancho + self.alto)

r = Rectangulo(5, 3)
print(r.area())
print(r.perimetro())

##Ejercicio 3

class Perro:
    def __init__(self, nombre, raza):
        self.nombre = nombre
        self.raza = raza

    def ladrar(self):
        print(f"{self.nombre} dice: ¡Guau!")

    def presentarse(self):
        print(f"Soy {self.nombre} y soy de raza {self.raza}")

perro = Perro("Rex", "Labrador")
perro.ladrar()
perro.presentarse()
print(perro.nombre)
print(perro.raza)

##Ejercicio 4

class Calculadora:

    @staticmethod
    def sumar(a, b):
        print(f"{a} + {b} = {a + b}")

    @staticmethod
    def restar(a, b):
        print(f"{a} - {b} = {a - b}")

    @staticmethod
    def multiplicar(a, b):
        print(f"{a} x {b} = {a * b}")

    @staticmethod
    def dividir(a, b):
        if b == 0:
            print("No se puede dividir entre 0")
        else:
            print(f"{a} / {b} = {a / b}")

calc = Calculadora()
calc.sumar(10, 5)
calc.restar(10, 5)
calc.multiplicar(10, 5)
calc.dividir(10, 0)

##Ejercicio 5

class CuentaBancaria:
    def __init__(self, saldo_inicial=0):
        self.__saldo = saldo_inicial  # atributo privado (encapsulamiento)

    def depositar(self, monto):
        self.__saldo += monto
        print(f"Depósito de ${monto}. Saldo: ${self.__saldo}")

    def retirar(self, monto):
        if monto > self.__saldo:
            print("Saldo insuficiente")
        else:
            self.__saldo -= monto
            print(f"Retiro de ${monto}. Saldo: ${self.__saldo}")

    def ver_saldo(self):
        print(f"Saldo actual: ${self.__saldo}")

cuenta = CuentaBancaria(100)
print("Revisión 1")
cuenta.ver_saldo()
cuenta.depositar(50)
print("Revisión 2")
cuenta.ver_saldo()
cuenta.retirar(200)
print("Revisión 3")
cuenta.ver_saldo()
cuenta.retirar(80)
print("Revisión 4")
cuenta.ver_saldo()


