def successor(n):
    return n | frozenset({n})

def show(n):
    parts = (show(k) for k in sorted(n, key=len))
    return "{" + ", ".join(parts) + "}"

# Строим числа 0, 1, 2, 3, 4:
numbers = [frozenset()]
for _ in range(4):
    numbers.append(successor(numbers[-1]))

# Печатаем числа как вложенные множества:
for index, number in enumerate(numbers):
    print(f"{index} = {show(number)}")  # «\cmo{1--5}»

# Сравниваем принадлежность и строгое включение:
m, n = numbers[2], numbers[4]
print("2 ∈ 4:", m in n)  # «\cmo{6}»
print("2 ⊊ 4:", m < n)   # «\cmo{7}»