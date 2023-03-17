estudiantes = []

for i in range(2):
    estudiante = {}

    estudiante['nombre'] = input("Ingrese su nombre ")
    estudiante['carnet'] = input("Ingrese su carnet ")
    estudiante['nota_final'] = int(input("Ingrese la nota final "))

    estudiantes.append(estudiante)

busqueda = 'mar123'
for e in estudiantes:
    if e['carnet'] == busqueda:
        print("El nombre del estudiantes es " +
              e['nombre'] + " y su nota final es " + str(e['nota_final']))
