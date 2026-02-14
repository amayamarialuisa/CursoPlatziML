#Tarea: investigar interacción con diccionarios (añadir, remover, quitar, cambiar...)

numbers = {1:"uno", 2:"dos", 3:"tres"}
print(numbers[2])

information = {"nombre": "Maria",
               "apellido": "Amaya",
               "edad": 27,
               "altura": 1.68,
               "sexo": "M"}

del information['sexo']
print(information)

claves = information.keys()
print(claves)
print(type(claves))
values = information.values()
print(values)
pairs = information.items()
print(pairs)

contacts = {"Maria": {"apellido": "Amaya",
               "edad": 27,
               "altura": 1.68,},
            "Diego":{"apellido": "Antezana",
                      "altura": 1.80,
                      "edad": 32,}}
print(contacts["Diego"])


