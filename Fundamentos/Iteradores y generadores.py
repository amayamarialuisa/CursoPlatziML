#Ejemplo de iterador

#Crear una lista
my_list = [1,2,3,4]

#Obtener el iterador
my_iter = iter(my_list)

#Usar el iterador
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))

text = "Hola mundo"
iter_text = iter(text)

for char in iter_text:
    print(char)

#Crear un iterador para números impares

#Limite
limit = 10

#Crear iterador
odd_itter = iter(range(1,limit+1,2))

#Usar el iterador
for num in odd_itter:
    print(num)

def my_generator():
    yield 1
    yield 2
    yield 3
for value in my_generator():
    print(value)

#Fibonacci
#0 1 1 2 3 5 8 13 21

