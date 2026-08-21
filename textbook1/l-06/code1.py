import math
import sys

def format_gaps(x):
    left = math.nextafter(x, -math.inf)
    right = math.nextafter(x, math.inf)
    return f"влево {x - left:.1e}, вправо {right - x:.1e}"

# Представление и диапазон конечных чисел:
m = sys.float_info.max
print(f"0.1 с 17 значащими цифрами: {0.1:.17g}")  # «\cmo{1}»
print(f"Крайние конечные float: {-m:.5e}, {m:.5e}")  # «\cmo{2}»

# Расстояния до соседних машинных чисел:
print(f"Шаг около 1: {format_gaps(1.0)}")  # «\cmo{3}»
print(f"Шаг около 1e16: {format_gaps(1e16)}")  # «\cmo{4}»

# Округление и специальные значения:
l = 1e16
i = math.inf
n = math.nan
print("1e16 + 1 == 1e16:", l + 1 == l)  # «\cmo{5}»
print("-inf < 0 < inf:", -i < 0 < i)  # «\cmo{6}»
print("inf + (-inf):", i + (-i))  # «\cmo{7}»
print("Сравнения с NaN:", n < 0, n == n, n > 0)  # «\cmo{8}»