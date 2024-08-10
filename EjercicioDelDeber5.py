# Crea un arreglo con 4 números de tu elección. Luego, escribe un código que sume estos números
# y muestre el resultado en la pantalla.

numeros = [25, 800, 540, 120, 220]
# Inicializar la variable suma
suma_total = 0
# Recorrer el arreglo y sumar cada número
for numero in numeros:
 suma_total += numero
# Mostrar el resultado de la suma
print("La suma de los números es:", suma_total)