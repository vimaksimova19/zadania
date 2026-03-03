# Определение функций, соответствующих уравнению 10cos(x) = 0.1x²
import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

def f(x):
# Разность левой и правой частей уравнения. Корни уравнения f(x) = 0 являются решением исходного уравнения.
    return 10 * math.cos(x) - 0.1 * x ** 2

def y_left(x):
# Левая часть уравнения: 10·cos(x)
    return 10 * math.cos(x)

def y_right(x):
# Правая часть уравнения: 0.1·x²
    return 0.1 * x ** 2

# Построение графиков обеих функций на отрезке [0, 10]
x_vals = np.linspace(0, 10, 500)                # 500 точек от 0 до 10
y_left_vals = [y_left(x) for x in x_vals]       # значения левой части
y_right_vals = [y_right(x) for x in x_vals]     # значения правой части

fig, ax = plt.subplots(figsize=(10, 6))          # создаём фигуру и оси
ax.plot(x_vals, y_left_vals, color='green', linewidth=2, label='y₁ = 10·cos(x)')
ax.plot(x_vals, y_right_vals, color='blue', linewidth=2, label='y₂ = 0.1·x²')

# Настройка сетки и подписей
ax.xaxis.set_major_locator(ticker.MultipleLocator(1))      # основные деления через 1
ax.xaxis.set_minor_locator(ticker.MultipleLocator(0.1))    # дополнительные через 0.1
plt.grid(True, which='both', alpha=0.3)                     # сетка
plt.xlabel('x', fontsize=12)
plt.ylabel('y', fontsize=12)
plt.title('График функций для отделения корней (вариант 10)', fontsize=14)
plt.legend()

# Отделение корней: поиск интервалов, где f(x) меняет знак
intervals = []           # список для хранения интервалов (a, b)
step = 0.1               # шаг поиска
x = 0.0                  # начальная точка

while x < 10:            # проходим по диапазону [0, 10]
    if f(x) * f(x + step) < 0:   # если значения разного знака
        intervals.append((x, x + step))   # запоминаем интервал
    x += step

print("Найденные интервалы, содержащие корни:")
for i, (a, b) in enumerate(intervals):
    print(f"  Интервал {i+1}: [{a:.3f}, {b:.3f}]")
# Уточнение корней методом половинного деления
roots = []               # список для найденных корней
eps = 0.001              # требуемая точность

for interval in intervals:
    a, b = interval
# Половинное деление до достижения точности
    while (b - a) > eps:
        c = (a + b) / 2           # середина отрезка
        if f(a) * f(c) <= 0:      # корень слева от c
            b = c
        else:                      # корень справа от c
            a = c
    root = (a + b) / 2            # итоговое приближение
    roots.append(root)

print("\nУточнённые значения корней (с точностью 0.001):")
for i, r in enumerate(roots):
    print(f"  Корень {i+1}: x = {r:.6f}")
# Отметим найденные корни на графике красными точками
y_roots = [y_left(r) for r in roots]  
ax.plot(roots, y_roots, 'ro', markersize=8, label='Корни уравнения')

# Добавим подписи возле точек
for i, r in enumerate(roots):
    ax.text(r, y_left(r) + 0.5, f'x={r:.3f}', fontsize=9, ha='center')

# Показываем график
plt.legend()
plt.tight_layout()
plt.show()