from fractions import Fraction
from math import ceil, floor

TWO = Fraction(2)

def decimal(q, digits=12, upper=False):
    scale = 10 ** digits
    scaled = ceil(q * scale) if upper else floor(q * scale)
    integer, tail = divmod(scaled, scale)
    return f"{integer},{tail:0{digits}d}"

def refine(left, right, steps=1):
    for _ in range(steps):
        middle = (left + right) / 2
        if middle * middle < TWO:
            left = middle
        else:
            right = middle
    return left, right

def show(n, left, right):
    left_text = decimal(left)
    right_text = decimal(right, upper=True)
    print(f"n={n:2d}: {left_text} < √2 < {right_text}")

left, right = Fraction(1), Fraction(2)

show(0, left, right)                # «\cmo{1}»

left, right = refine(left, right)
show(1, left, right)                # «\cmo{2}»

left, right = refine(left, right)
show(2, left, right)                # «\cmo{3}»

left, right = refine(left, right, steps=3)
show(5, left, right)                # «\cmo{4}»

left, right = refine(left, right, steps=5)
show(10, left, right)               # «\cmo{5}»

left, right = refine(left, right, steps=10)
show(20, left, right)               # «\cmo{6}»

left, right = refine(left, right, steps=20)
show(40, left, right)               # «\cmo{7}»