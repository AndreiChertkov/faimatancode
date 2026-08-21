from itertools import accumulate
from math import pi

def partial_sums(power, last):
    terms = (1 / k**power for k in range(1, last + 1))
    return [0.0, *accumulate(terms)]

indices = (10, 100, 1000, 10_000)
last = 2 * indices[-1]

q_sums = partial_sums(2, last)
h_sums = partial_sums(1, last)

row_format = "{:5d} | {:9.2e} | {:9.3f} | {:8.2e} | {:8.2e}"

print("    n | Q_2n-Q_n | H_2n-H_n | ΔQ_n     | ΔH_n")  # «\cmo{1}»
for n in indices:
    q_gap = q_sums[2 * n] - q_sums[n]
    h_gap = h_sums[2 * n] - h_sums[n]
    q_step = q_sums[n + 1] - q_sums[n]
    h_step = h_sums[n + 1] - h_sums[n]
    print(row_format.format(
        n, q_gap, h_gap, q_step, h_step))  # «\cmo{2--5}»