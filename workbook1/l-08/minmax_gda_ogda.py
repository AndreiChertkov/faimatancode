import matplotlib.pyplot as plt
import numpy as np

# ============================================================
# 1. TODO: implement GDA
# ============================================================

def run_gda(x0, y0, eta, steps):
    """
    Gradient Descent/Ascent для f(x, y) = xy.

    Правило обновления:
        x_{n+1} = x_n - eta * y_n
        y_{n+1} = y_n + eta * x_n

    Возвращает:
    points -- массив формы (steps + 1, 2).
    """
    # TODO: реализуйте функцию
    pass


# ============================================================
# 2. TODO: implement simplified OGDA
# ============================================================

def run_simplified_ogda(x0, y0, eta, steps):
    """
    Упрощённая предсказательная модель OGDA.

    Правило обновления:
        x_{n+1} = (1 - eta^2) * x_n - eta * y_n
        y_{n+1} = eta * x_n + (1 - eta^2) * y_n

    Возвращает:
    points -- массив формы (steps + 1, 2).
    """
    # TODO: реализуйте функцию
    pass


# ============================================================
# 3. TODO: distance to equilibrium
# ============================================================

def distances_to_zero(points):
    """Считает r_n = sqrt(x_n^2 + y_n^2)."""
    # TODO: реализуйте функцию
    pass


# ============================================================
# 4. TODO: numerical Cauchy check
# ============================================================

def tail_diameter(points, start_index):
    """
    Считает диаметр хвоста:
        max ||points[i] - points[j]||
    по всем i, j >= start_index.

    Это конечный численный аналог критерия Коши.
    """
    # TODO: реализуйте функцию
    pass


def find_cauchy_start(points, epsilon, min_tail_length=20):
    """
    Пытается найти индекс N, начиная с которого хвост
    имеет диаметр меньше epsilon.

    Так как траектория конечна, требуем, чтобы в хвосте
    было не меньше min_tail_length точек.

    Возвращает:
    первый подходящий индекс N или None.
    """
    # TODO: реализуйте функцию
    pass


# ============================================================
# 5. Run experiment
# ============================================================

x0 = 1.0
y0 = 0.0

steps = 200

eta_gda = 0.2
eta_ogda = 0.5

points_gda = run_gda(
    x0=x0,
    y0=y0,
    eta=eta_gda,
    steps=steps,
)

points_ogda = run_simplified_ogda(
    x0=x0,
    y0=y0,
    eta=eta_ogda,
    steps=steps,
)

r_gda = distances_to_zero(points_gda)
r_ogda = distances_to_zero(points_ogda)


# ============================================================
# 6. Cauchy check
# ============================================================

epsilon = 1e-3

gda_cauchy_start = find_cauchy_start(
    points=points_gda,
    epsilon=epsilon,
    min_tail_length=20,
)

ogda_cauchy_start = find_cauchy_start(
    points=points_ogda,
    epsilon=epsilon,
    min_tail_length=20,
)

print("epsilon =", epsilon)
print("GDA Cauchy start:", gda_cauchy_start)
print("Simplified OGDA Cauchy start:", ogda_cauchy_start)

print()
print("Final GDA distance:", r_gda[-1])
print("Final simplified OGDA distance:", r_ogda[-1])


# ============================================================
# 7. Plot distances r_n
# ============================================================

n = np.arange(steps + 1)

plt.figure(figsize=(9, 5))
plt.semilogy(n, r_gda, label=f"GDA, eta={eta_gda}")
plt.semilogy(n, r_ogda, label=f"Simplified OGDA, eta={eta_ogda}")
plt.xlabel("iteration n")
plt.ylabel("r_n")
plt.title("Distance to equilibrium")
plt.legend()
plt.grid(True)
plt.show()


# ============================================================
# 8. Plot trajectories
# ============================================================

plt.figure(figsize=(6, 6))
plt.plot(points_gda[:, 0], points_gda[:, 1], marker="o", markersize=3, label="GDA")
plt.plot(points_ogda[:, 0], points_ogda[:, 1], marker="o", markersize=3, label="Simplified OGDA")
plt.scatter([0], [0], s=80, label="equilibrium")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Trajectories in the (x, y)-plane")
plt.legend()
plt.grid(True)
plt.axis("equal")
plt.show()


# ============================================================
# 9. Optional: tail diameters
# ============================================================

tail_starts = np.arange(0, steps - 20)

gda_diameters = np.array([
    tail_diameter(points_gda, start)
    for start in tail_starts
])

ogda_diameters = np.array([
    tail_diameter(points_ogda, start)
    for start in tail_starts
])

plt.figure(figsize=(9, 5))
plt.semilogy(tail_starts, gda_diameters, label="GDA tail diameter")
plt.semilogy(tail_starts, ogda_diameters, label="Simplified OGDA tail diameter")
plt.axhline(epsilon, linestyle="--", label="epsilon")
plt.xlabel("tail start index")
plt.ylabel("tail diameter")
plt.title("Numerical Cauchy check")
plt.legend()
plt.grid(True)
plt.show()
