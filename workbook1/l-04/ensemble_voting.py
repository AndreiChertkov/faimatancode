from math import comb

import matplotlib.pyplot as plt


def p_true(n, p):
    """
    Вероятность правильного ответа ансамбля из n классификаторов
    при голосовании большинством (n нечётно, ничьей нет).
    """
    # TODO: реализуйте по формуле из пункта 3.
    pass


def check_total_probability(n, p):
    """
    Проверка, что сумма вероятностей P(K=k) для k=0,...,n равна 1.
    """
    # TODO: реализуйте проверку по формуле биномиального распределения.
    pass


for n in [1, 3, 5, 11, 21]:
    print(n, check_total_probability(n, 0.6))

# ============================================================
# Поведение ансамбля при p > 0.5
# ============================================================

p = 0.55

n_values = list(range(1, 101, 2))
probabilities = [p_true(n, p) for n in n_values]

plt.figure(figsize=(8, 5))
plt.plot(n_values, probabilities)
plt.xlabel("n")
plt.ylabel("P_true(n, p)")
plt.title("Probability of correct ensemble answer when p > 0.5")
plt.grid(True)
plt.show()
