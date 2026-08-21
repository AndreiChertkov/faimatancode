from fractions import Fraction
from math import ceil, floor

def bounds(n):
    base = Fraction(n + 1, n)
    lower = base ** n
    upper = lower * base
    return lower, upper

def decimal(q, digits=10, up=False):
    scale = 10 ** digits
    scaled = ceil(q * scale) if up else floor(q * scale)
    integer, tail = divmod(scaled, scale)
    return f"{integer},{tail:0{digits}d}"

indices = (1, 2, 5, 10, 100, 1000, 10_000, 100_000, 1_000_000)

for n in indices:
    lower, upper = bounds(n)
    
    left = decimal(lower)
    right = decimal(upper, up=True)
    
    print(f"n={n:8d}: {left} < e < {right}")  # «\cmo{1--9}»