import itertools

def variaciones_con_repeticion(elementos, k):
    # itertools.product genera combinaciones con repetición y orden
    return list(itertools.product(elementos, repeat=k))

# Ejemplo de uso
elementos = ['A', 'B', 'C']
k = 2

variaciones = variaciones_con_repeticion(elementos, k)

print(f"Variaciones con repetición de {elementos} tomando {k}:")
for v in variaciones:
    print(v)

print(f"\nTotal de variaciones: {len(variaciones)}")