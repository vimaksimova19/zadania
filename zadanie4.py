# Определение целевой функции и её производных f(x) = 10·cos(x) - 0.1·x²
import math
import sympy as sp

def f(x):
    return 10 * math.cos(x) - 0.1 * x ** 2

# Производные понадобятся для проверки условий сходимости и в методе Ньютона
def f_derivative(x):
    """
    Первая производная f'(x) = -10·sin(x) - 0.2·x
    """
    return -10 * math.sin(x) - 0.2 * x

def f_derivative2(x):
    """
    Вторая производная f''(x) = -10·cos(x) - 0.2
    """
    return -10 * math.cos(x) - 0.2

# Отделение корней (поиск интервалов, содержащих корни). Будем искать корни на отрезке [0, 10] с шагом 0.1
intervals = []
step = 0.1
x = 0.0
while x < 10:
    if f(x) * f(x + step) < 0:
        intervals.append((x, x + step))
    x += step

print("Найденные интервалы, содержащие корни:")
for i, (a, b) in enumerate(intervals):
    print(f"  Интервал {i+1}: [{a:.3f}, {b:.3f}]")
print()

# Аналитическое выражение функции и её производных
x_sym = sp.Symbol('x')
f_expr = 10 * sp.cos(x_sym) - 0.1 * x_sym ** 2
f_derivative1_expr = sp.diff(f_expr, x_sym)
f_derivative2_expr = sp.diff(f_derivative1_expr, x_sym)
print("Символьное представление:")
print("  f(x)  =", f_expr)
print("  f'(x) =", f_derivative1_expr)
print("  f''(x) =", f_derivative2_expr)
print()

# 3. Вспомогательная функция для оценки погрешности. Метод хорд (секущих)
def secant_step(c, x):
# Один шаг метода хорд для закреплённой точки c и текущего приближения x. Формула: x_{n+1} = x - f(x) * (x - c) / (f(x) - f(c))
    return x - f(x) * (x - c) / (f(x) - f(c))

# Список для хранения результатов
roots_sec = []       # найденные корни
iters_sec = []       # число итераций для каждого корня
eps = 0.001          # требуемая точность

print("Метод хорд:")
for (a, b) in intervals:
    # Вычисляем на интервале
    m = min(abs(f_derivative(a)), abs(f_derivative(b)))
    
    # Определяем, какой конец интервала будет закреплённым (c), а какой подвижным (x)
    if f(a) * f_derivative2(a) > 0:
        c, x = a, b          # закрепляем a, подвижная точка b
    else:
        c, x = b, a          # закрепляем b, подвижная точка a
    
    iter_count = 0
    while True:
        x_new = secant_step(c, x)
        iter_count += 1
        # Критерий остановки: |f(x_new)| / m < eps
        if abs(f(x_new)) / m < eps:
            roots_sec.append(x_new)
            iters_sec.append(iter_count)
            print(f"  Корень на [{a:.3f}, {b:.3f}] = {x_new:.6f}, достигнут за {iter_count} итераций")
            break
        x = x_new

print()

# Метод касательных (Ньютона)
def newton_step(x):
# Один шаг метода Ньютона: x_{n+1} = x - f(x) / f'(x)
    return x - f(x) / f_derivative(x)

roots_newton = []
iters_newton = []

print("Метод касательных (Ньютона):")
for (a, b) in intervals:
    m = min(abs(f_derivative(a)), abs(f_derivative(b)))
    
# Выбор начального приближения: Если f(a) * f''(a) > 0, начинаем с a, иначе с b.
    if f(a) * f_derivative2(a) > 0:
        x = a
    else:
        x = b
    
    iter_count = 0
    while True:
        x_new = newton_step(x)
        iter_count += 1
        if abs(f(x_new)) / m < eps:
            roots_newton.append(x_new)
            iters_newton.append(iter_count)
            print(f"  Корень на [{a:.3f}, {b:.3f}] = {x_new:.6f}, достигнут за {iter_count} итераций")
            break
        x = x_new

print()

# Итоговые результаты
print("Итоговые результаты")
print(f"{'Интервал':<15} {'Метод хорд':<20} {'Метод Ньютона':<20}")
for i, (a, b) in enumerate(intervals):
    print(f"[{a:.3f}, {b:.3f}]    {roots_sec[i]:.6f} (за {iters_sec[i]} итер.)    {roots_newton[i]:.6f} (за {iters_newton[i]} итер.)")