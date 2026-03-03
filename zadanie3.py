# Определение исходной функции f(x) = 10·cos(x) - 0.1·x²
import math
import sympy as sp
from sympy import cos, Eq, solve, acos, diff

def f(x):
    return 10 * math.cos(x) - 0.1 * x ** 2
# Проверка существования корня на отрезке [1.5, 1.55]
a, b = 1.5, 1.55
fa = f(a)
fb = f(b)
print(f"f({a}) = {fa:.6f}, f({b}) = {fb:.6f}")
if fa * fb < 0:
    print(f"Корень существует на отрезке [{a}; {b}] (функция меняет знак).")
else:
    print("Корень не существует на данном отрезке (нет смены знака).")
print()
# Преобразование уравнения к виду x = φ(x) для метода итераций
x_sym = sp.Symbol('x', real=True)
# Левая и правая части уравнения в символьном виде
left_expr = 10 * sp.cos(x_sym)
right_expr = 0.1 * x_sym ** 2
# Составляем уравнение left = right
equation = Eq(left_expr, right_expr)
print("Символьное уравнение:", equation)

#Запишем итерационную функцию: ф(x) = arccos(0.01·x²)
phi_expr = sp.acos(0.01 * x_sym ** 2)
print("Итерационная функция φ(x) =", phi_expr)

# Вычисление производной ф'(x) для проверки условия сходимости
phi_derivative = sp.diff(phi_expr, x_sym)
print("Производная φ'(x) =", phi_derivative)
print()

# Определение итерационной функции для численных расчётов
def phi(x):
    """Численная реализация φ(x) = arccos(0.01·x²)"""
    return math.acos(0.01 * x * x)   

# Проверка условия сходимости |ф'(x)| < 1 на отрезке [1.5, 1.55]
# Аналитическое выражение производной 
def dphi(x):
    """Численное значение производной φ'(x)"""
    t = 0.01 * x * x
    denominator = math.sqrt(1 - t*t)
    return -0.02 * x / denominator

# Вычисляем модуль производной на концах отрезка
dphi_a = abs(dphi(a))
dphi_b = abs(dphi(b))
max_dphi = max(dphi_a, dphi_b)
print(f"|φ'({a})| = {dphi_a:.6f}, |φ'({b})| = {dphi_b:.6f}")
if max_dphi < 1:
    print(f"Условие сходимости выполняется: максимум |φ'| на отрезке = {max_dphi:.6f} < 1")
else:
    print(f"Условие сходимости НЕ выполняется: максимум |φ'| = {max_dphi:.6f} >= 1")
print()

# Метод простой итерации
x0 = (a + b) / 2   # 1.525
print(f"Начальное приближение: x0 = {x0}")
eps = 0.001
iter_count = 0
x_prev = x0

print("\nИтерации:")
while True:
    x_next = phi(x_prev)
    iter_count += 1
    diff = abs(x_next - x_prev)
    print(f"Итерация {iter_count}: x_{iter_count} = {x_next:.6f}, |x_{iter_count} - x_{iter_count-1}| = {diff:.6f}")
    if diff < eps:
        root = x_next
        break
    x_prev = x_next

print(f"\nКорень уравнения с точностью {eps}: x = {root:.6f} (найден на {iter_count}-й итерации)")