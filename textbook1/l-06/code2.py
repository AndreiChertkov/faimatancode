from fractions import Fraction
from math import ceil, floor

def decimal(q, digits=12, upper=False):
    scale = 10 ** digits
    scaled = ceil(q * scale) if upper else floor(q * scale)
    integer, tail = divmod(scaled, scale)
    return f"{integer},{tail:0{digits}d}"

def refine_decimal(q, left, right, steps=1):
    for _ in range(steps):
        step = (right - left) / 10
        digit = (q - left) // step
        left = left + digit * step
        right = left + step
    return left, right

def show_interval(n, left, right):
    if n == 0:
        print(f"n={n}: I_{n} = [{left}; {right}]")
        return
    left_text = decimal(left, digits=n)
    right_text = decimal(right, digits=n, upper=True)
    print(f"n={n}: I_{n} = [{left_text}; {right_text}]")

print("---> Локализация 1/7; I_0 = [0, 1]")       # «\cmo{1}»
q = Fraction(1, 7)
left, right = Fraction(0), Fraction(1)
show_interval(0, left, right)                     # «\cmo{2}»
left, right = refine_decimal(q, left, right)
show_interval(1, left, right)                     # «\cmo{3}»
left, right = refine_decimal(q, left, right)
show_interval(2, left, right)                     # «\cmo{4}»
left, right = refine_decimal(q, left, right, steps=4)
show_interval(6, left, right)                     # «\cmo{5}»
left, right = refine_decimal(q, left, right, steps=6)
show_interval(12, left, right)                    # «\cmo{6}»

print("---> Локализация 22/7; I_0 = [3, 4]")      # «\cmo{7}»
q = Fraction(22, 7)
left, right = Fraction(3), Fraction(4)
left, right = refine_decimal(q, left, right, steps=6)
show_interval(6, left, right)                     # «\cmo{8}»
left, right = refine_decimal(q, left, right, steps=6)
show_interval(12, left, right)                    # «\cmo{9}»