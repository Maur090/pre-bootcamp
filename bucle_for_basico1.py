for i in range(101):
    print(i)
# Básico

for i in range(2, 500, 2):
    print(i)
# Múltiples de 2

for i in range(1, 101):
    if i % 10 == 0:
        print("baby")
    elif i % 5 == 0:
        print("ice ice")
    else:
        print(i)
# Contando Vanilla Ice

suma = 0
for i in range(0, 500001, 2):
    suma += i
print(suma)
#Wow. Número gigante a la vista

for i in range(2024, 0, -3):
    print(i)
# Regrésame al 3

numInicial = 3
numFinal = 10
multiplo = 2

for i in range(numInicial, numFinal + 1):
    if i % multiplo == 0:
        print(i)
#Contador dinámico