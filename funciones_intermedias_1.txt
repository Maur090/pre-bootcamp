#1. Actualizar valores en diccionarios y listas
matriz = [ [10, 15, 20], [6, 7, 14] ]
cantantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"}
]

ciudades = {
    "México": ["Ciudad de México", "Guadalajara", "Cancún"],
    "Chile": ["Santiago", "Concepción", "Viña del Mar"]
}

coordenadas = [
    {"latitud": 8.2588997, "longitud": -84.9399704}
]

def cambiar_valor_matriz(matriz, valor_antiguo, valor_nuevo):
    for fila in matriz:
        for i in range(len(fila)):
            if fila[i] == valor_antiguo:
                fila[i] = valor_nuevo
matriz = [[10, 15, 20], [3, 7, 14]]
cambiar_valor_matriz(matriz, 3, 6)
print(matriz)

def cambiar_nombre_primer_cantante(cantantes, nuevo_nombre):
    if cantantes and "nombre" in cantantes[0]:
        cantantes[0]["nombre"] = nuevo_nombre
cantantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"}
]
cambiar_nombre_primer_cantante(cantantes, "Enrique Martin Morales")
print(cantantes)

def cambiar_ciudad(ciudades, pais, ciudad_antigua, ciudad_nueva):
    if pais in ciudades:
        for i in range(len(ciudades[pais])):
            if ciudades[pais][i] == ciudad_antigua:
                ciudades[pais][i] = ciudad_nueva
cambiar_ciudad(ciudades, "México", "Cancún", "Monterrey")
print(ciudades)

def cambiar_latitud(coordenadas, nueva_latitud):
    if coordenadas and "latitud" in coordenadas[0]:
        coordenadas[0]["latitud"] = nueva_latitud
cambiar_latitud(coordenadas, 9.9355431)
print(coordenadas)

#2. Iterar a través de una lista de diccionarios

def iterarDiccionario(lista_diccionarios):
    for dic in lista_diccionarios:
        for clave, valor in dic.items():
            print(f"{clave}: {valor}")

cantantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"},
    {"nombre": "José José", "pais": "México"},
    {"nombre": "Juan Luis Guerra", "pais": "República Dominicana"}
]
iterarDiccionario(cantantes)

def iterarDiccionario(lista_diccionarios):
    for dic in lista_diccionarios:
        print(f"nombre - {dic['nombre']}, pais - {dic['pais']}")

cantantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"},
    {"nombre": "José José", "pais": "México"},
    {"nombre": "Juan Luis Guerra", "pais": "República Dominicana"}
]
iterarDiccionario(cantantes)

# 3. Obtener valores de una lista de diccionarios

def iterarDiccionario2(llave, lista):
    for dic in lista:
        if llave in dic:
            print(dic[llave])
iterarDiccionario2("nombre", cantantes)


def iterarDiccionario2(llave, lista):
    for dic in lista:
        if llave in dic:
            print(dic[llave])
iterarDiccionario2("pais", cantantes)

# 4. Iterar a través de un diccionario con valores de lista

costa_rica = {
    "ciudades": ["San José", "Limón", "Cartago", "Puntarenas"],
    "comidas": ["gallo pinto", "casado", "tamales", "chifrijo", "olla de carne"]
}

def imprimirInformacion(diccionario):
    for clave, lista in diccionario.items():
        print(f"{len(lista)} {clave.upper()}")
        for valor in lista:
            print(valor)
        print() 
imprimirInformacion(costa_rica)