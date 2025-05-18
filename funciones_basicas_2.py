def lista_multiplicados_por_dos(num):
    return [i * 2 for i in range(num + 1)]
print(lista_multiplicados_por_dos(5))
# Multiplica por 2

def suma_y_resta(lista):
    suma = lista[0] + lista[1]
    print(suma)
    return lista[0] - lista[1]
resultado = suma_y_resta([5, 4])
print("Resta:", resultado)
# Suma y resta

def sumatoria_menos_longitud(lista):
    return sum(lista) - len(lista)
resultado = sumatoria_menos_longitud([1, 2, 3, 4])
print(resultado)
# Sumatoria menos longitud

def valores_multiplicados_segundo(lista):
    print(len(lista))
    if len(lista) < 2:
        return []
    segundo = lista[1]
    nueva_lista = [x * segundo for x in lista]
    return nueva_lista
print(valores_multiplicados_segundo([1, 3, 5, 7]))
print(valores_multiplicados_segundo([1]))
# Valores multiplicados por el segundo

def lista_valores(valor, longitud):
    return [valor * longitud] * longitud
print(lista_valores(5, 2))
print(lista_valores(7, 5))
# Valor multiplado y longitud