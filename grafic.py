import numpy as np          # библиотека для математических операций
import matplotlib.pyplot as plt   # библиотека для построения графиков

# Определяем функцию
def f(x):
    return 10 * np.cos(x) - 0.1 * x**2

# Создаём 500 точек на отрезке от 0 до 10
x = np.linspace(0, 10, 500)
# Вычисляем значения функции в этих точках
y = f(x)

# Строим график
plt.plot(x, y, label='f(x) = 10·cos(x) - 0.1·x²', color='blue')
plt.axhline(0, color='black', linestyle='--', linewidth=0.8)  # ось X
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('График функции')
plt.grid(True)
plt.legend()
plt.show()