from fractions import Fraction

neurons = [(1, 0, 1), (1, -1, -2), (1, -2, 1)]
bias = Fraction(0)

def network(x):
    return bias + sum(
        c * max(0, a * x + b) for a, b, c in neurons)

L = sum(abs(c * a) for a, b, c in neurons)
x = Fraction(1)
eps = Fraction(1, 10)
value = network(x)
delta = eps / L

print(f"N({x}) = {value}; L = {L}")       # «\cmo{1}»
print(f"ε = {eps}; δ = {delta}")          # «\cmo{2}»
print("    h |  |ΔN| |  L|h| | |h| < δ")  # «\cmo{3}»

for h in map(Fraction, ("-1/20", "-1/50", "1/50", "1/20")):
    change = abs(network(x + h) - value)
    bound = L * abs(h)
    
    ok = delta is None or abs(h) < delta
    
    row = f"{str(h):>5} | {str(change):>5}"
    row += f" | {str(bound):>5} | {'да' if ok else 'нет'}"
    print(row)  # «\cmo{4--7}»