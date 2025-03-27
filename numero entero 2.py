'''
n = int(input ("Ingrese un numero "))

resultado = int((n * (n+1)) / 2)

print("La sumatoria de numeros desde 1 hasta " + str(n) + " es: " + str(resultado))
'''

numero = int(input("Ingresa un numero: "))

while numero<0:
    print("Error -> Deberia ser un numero positivo")
    numero = int(input("Ingrese un numero: "))

resultado = int((numero * (numero+1)) / 2)

print("La sumatoria de numeros desde 1 hasta " + str(numero) + " es: " + str(resultado))
