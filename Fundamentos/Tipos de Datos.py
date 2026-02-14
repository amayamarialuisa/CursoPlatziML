#Operadores numéricos

inscripciones = [
    ("Ana", "Python"),
    ("Luis", "Python"),
    ("Ana", "Estadística"),
    ("Carlos", "Machine Learning"),
    ("Luis", "Estadística"),
    ("Ana", "Python"),
    ("María", "Machine Learning"),
    ("Carlos", "Python")
]

#Un ciclo itera sobre una estructura de datos con una condición X. Hay dos tipos for while. For es para una estructura
#de datos finita y while mientras una condición se cumpla

estudiantes = {}

for nombre, curso in inscripciones:
    if nombre not in estudiantes:
        estudiantes[nombre] = set()

    estudiantes[nombre].add(curso)

print("Cursos por estudiante")
for nombre, cursos in estudiantes.items():
    print(f"{nombre}: {len(cursos)} cursos -> {cursos}")

python_estudiantes = set()
for nombre, cursos in estudiantes.items():
    if "Python" in cursos:
        python_estudiantes.add(nombre)

print(f"Estudiantes que tomaron Python: {python_estudiantes}")