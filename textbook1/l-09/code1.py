import math

def f(x):
    return math.sin(math.pi * x)

indices = (1, 10, 100, 1000, 10_000)

# Три сетки аргументов, уходящих на +∞:
# x_n = n,  y_n = 2n + 1/2,  z_n = 2n + 3/2
print("    n | f(x_n)   | f(y_n) | f(z_n)")  # «\cmo{1}»
for n in indices:
    q = f(n)
    v = f(2 * n + 0.5)
    w = f(2 * n + 1.5)
    print(f"{n:5d} | {q:+.1e} |{v:+7.1f} |{w:+7.1f}") # «\cmo{2--6}»