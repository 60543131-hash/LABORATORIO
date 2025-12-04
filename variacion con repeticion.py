import itertools

# Pedir datos al usuario
n = int(input("Cantidad de elementos (n): "))
k = int(input("Longitud de cada variación (k): "))

# Leer los elementos
elementos = []
print("Ingresa los elementos uno por uno:")
for i in range(n):
    elem = input(f"Elemento {i+1}: ")
    elementos.append(elem)

# Generar variaciones con repetición
variaciones = itertools.product(elementos, repeat=k)

print("\nVariaciones con repetición:")
for v in variaciones:
    print(v)