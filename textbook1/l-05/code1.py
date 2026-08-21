from fractions import Fraction

def h(x):
    x = Fraction(x)
    return x / (1 + abs(x))

def h_inverse(t):
    t = Fraction(t)
    if abs(t) >= 1:
        raise ValueError("Ожидалось t из интервала (-1, 1)")
    return t / (1 - abs(t))

def l(t):
    t = Fraction(t)
    return (1 + t) / 2

def l_inverse(y):
    y = Fraction(y)
    if not 0 < y < 1:
        raise ValueError("Ожидалось y из интервала (0, 1)")
    return 2 * y - 1

def f(x):
    return l(h(x))

def g(y):
    return h_inverse(l_inverse(y))

points = (
    Fraction(1, 2_000_000),
    Fraction(1, 20),
    Fraction(1, 4),
    Fraction(1, 2),
    Fraction(3, 4),
    Fraction(19, 20),
    Fraction(1_999_999, 2_000_000),
)

print("Отображение g: (0, 1) -> R")               # «\cmo{1}»
for y in points:
    print(f"g({y}) = {g(y)}")                     # «\cmo{2--8}»

line_points = (-10**6, -999, -1, 0, 1, 999, 10**6)
check_y = all(f(g(y)) == y for y in points)
check_x = all(g(f(x)) == x for x in line_points)

print("Проверка f(g(y)) = y:", check_y)           # «\cmo{9}»
print("Проверка g(f(x)) = x:", check_x)           # «\cmo{10}»