from fractions import Fraction
from math import ceil, floor

def decimal(q, digits, upper=False):
    scale = 10 ** digits
    scaled = ceil(q * scale) if upper else floor(q * scale)
    integer, tail = divmod(scaled, scale)
    return f"{integer}.{tail:0{digits}d}"

def limit_bounds(eps):
    eps = Fraction(eps)
    if eps <= 0:
        raise ValueError("Точность должна быть положительной")

    # Шаг печати не больше одной десятой допустимой ширины:
    digits = 0
    while Fraction(10, 10 ** digits) > eps:
        digits += 1
    step = Fraction(1, 10 ** digits)

    # Резервируем два шага на округление границ:
    n = ceil(1 / (eps - 2 * step))
    terms = (Fraction(1, k * k) for k in range(1, n + 1))
    total = sum(terms, Fraction(0))
    return n, total, total + Fraction(1, n), digits

# Строки задают десятичные числа точно, без участия float:
for eps in ("0.01", "0.001"):
    n, lower, upper, digits = limit_bounds(eps)
    left = decimal(lower, digits)
    right = decimal(upper, digits, upper=True)
    text = f"ε={eps}: N={n:4d}; L ∈ [{left}, {right}]"
    print(text)  # «\cmo{1--2}»