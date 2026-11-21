from fractions import Fraction

def bisect(f, a, b, eps):
    a, b, eps = map(Fraction, (a, b, eps))
    if a >= b or eps <= 0:
        raise ValueError("Нужны a < b и eps > 0")
    fa, fb = f(a), f(b)
    if fa * fb >= 0:
        raise ValueError("Нужны разные знаки на концах")

    steps = 0
    while b - a > 2 * eps:
        m = (a + b) / 2
        fm = f(m)
        steps += 1
        if fm == 0:
            return m, m, steps
        if fa * fm < 0:
            b = m
        else:
            a, fa = m, fm
    return a, b, steps

def f(x):
    return x**5 + x - 1

eps = Fraction(1, 8192)
a, b, steps = bisect(f, 0, 1, eps)
z, error = (a + b) / 2, (b - a) / 2

print(f"Шагов бисекции: {steps}")          # «\cmo{1}»
print(f"Отрезок: [{a}, {b}]")              # «\cmo{2}»
print(f"Приближение: {z}")                 # «\cmo{3}»
print(f"Граница погрешности: {error}")     # «\cmo{4}»