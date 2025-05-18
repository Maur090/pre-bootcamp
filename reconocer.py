numero1 = 70 # declaración de variable [int] entero 
numero2 = 3.14 # declaración de variable [float] decimal
booleano:bool = False # declaración de variable [bool] booleano
cadena:str = 'Hola Mundo' # declaración de variable [str] cadena
ingredientes_pastel = ['Harina', 'Leche', 'Huevos', 'Vainilla', 'Chocolate'] # declaración de variable [list <str>] lista
persona = {'nombre': 'Patricio', 'pais': 'México', 'edad': 35, 'soltero': False} # declaración de variable [dict] diccionario
frutas = ('guayaba', 'fresa', 'papaya') # declaración de variable [tuple] tupla
print(type(frutas)) # revisión de tipo
print(ingredientes_pastel[2]) # revisión de tipo
ingredientes_pastel.append('Mantequilla')
print(persona['nombre']) # revisión de tipo
persona['nombre'] = 'Kevin'
persona['color_ojos'] = 'cafe'
print(frutas[2]) # revisión de tipo

if numero1 > 45:
    print("Numero mayor")# revisión de tipo
else:
    print("Numero menor")# revisión de tipo

if len(cadena) < 5:
    print("Cadena corta")# revisión de tipo
elif len(cadena) > 15:
    print("Cadena larga")# revisión de tipo
else:
    print("Cadena perfecta")# revisión de tipo

for x in range(8):
    print(x)# revisión de tipo
for x in range(2,8):
    print(x)# revisión de tipo
for x in range(2,8,2):
    print(x)# revisión de tipo
x = 0
while(x < 8):
    print(x)# revisión de tipo
    x += 1

ingredientes_pastel.pop()
ingredientes_pastel.pop(1)

print(persona)# revisión de tipo
persona.pop('color_ojos')
print(persona)# revisión de tipo

for ingrediente in ingredientes_pastel:
    if ingrediente == 'Harina':
        continue
    print('Después de la primera sentencia')# revisión de tipo
    if ingrediente == 'Chocolate':
        break

def imprime_hola_10_veces():
    for numero in range(10):
        print('Hola')# revisión de tipo

imprime_hola_10_veces()

def imprime_hola_n_veces(n):
    for numero in range(n):
        print('Hola')# revisión de tipo

imprime_hola_n_veces(5)

def imprime_hola_n_o_diez_veces(n = 10):
    for numero in range(n):
        print('Hola')# revisión de tipo

imprime_hola_n_o_diez_veces()
imprime_hola_n_o_diez_veces(5)


"""
Sección BONUS
"""

# print(numero3)
# numero3 = 86
# frutas[0] = 'naranja'
# print(persona['hobbies'])
# print(ingredientes_pastel[11])
#   print(booleano)
# frutas.append('manzana')
# frutas.pop(1)