
import matplotlib.pyplot as plt
import numpy as np

# Función del valor del automóvil
def P(t):
    return -30000 * t + 300000

# Rango de tiempo de 0 a 5 años
t = np.linspace(0, 5, 100)
valor = P(t)

# Crear la gráfica
plt.plot(t, valor, linewidth=2)
plt.title("Desvalorización de un Automóvil con el Tiempo")
plt.xlabel("Tiempo (años)")
plt.ylabel("Valor del automóvil (pesos)")
plt.grid(True)

# Mostrar la gráfica
plt.show()
