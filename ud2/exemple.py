# Definició de variables
inici = 1
final = 10

# Bucle per iterar des de 'inici' fins a 'final'
for num in range(inici, final + 1):
    # Condicional per comprovar si el nombre és imparell
    if num % 2 != 0:
        print(f"{num} és imparell")
    else:
        print(f"{num} és parell")
