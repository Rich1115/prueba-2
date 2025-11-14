import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

x= int(input())
y=[]
for i in range (100):
    y.append(i+1)
print(y)

par=[]
impar=[]

for numero in y:
    if numero % 2 == 0:
        par.append(numero)
    else:
        impar.append(numero)

print("Pares:", par)
print("Impares:", impar)

plt.figure(figsize=(10, 5))

# Gráfico de pares
plt.plot(par, label="Pares", marker='o')

# Gráfico de impares
plt.plot(impar, label="Impares", marker='x')

plt.title("Gráfico de números pares e impares")
plt.xlabel("Índice")
plt.ylabel("Valor")
plt.legend()
plt.grid(True)

plt.show()