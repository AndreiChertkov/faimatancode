from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

# Сначала завершите и запустите шаблон практики 11.
data_path = (
    Path(__file__).resolve().parents[1] / "l-11" / "digits_path.npz"
)
if not data_path.exists():
    raise FileNotFoundError(
        "Сначала запустите decision_continuity.py из практики 11."
    )
with np.load(data_path, allow_pickle=False) as data:
    a, b, c = data["a"], data["b"], data["c"]
    d, L = float(data["d"]), float(data["L"])
    u, v = data["u"], data["v"]

def score(t):
    return float(d + np.sum(c * np.maximum(a * t + b, 0)))

def answer(t):
    return 3 if score(t) < 0 else 8

def bisect_zero(score, left, right, eps):
    """
    При F(left) < 0 < F(right) и eps > 0 найдите отрезок,
    содержащий ноль, длиной не больше 2 * eps.
    Верните (левый конец, правый конец, число шагов).
    При точном попадании в ноль верните его в обоих концах.
    """
    # TODO: реализуйте половинное деление из пункта 3.
    pass

def check_interval(score, L, A, B, N):
    """
    Для N равных частей отрезка [A, B] верните:
    (mu_h, нижняя оценка mu, подтверждено ли постоянство ответа).
    """
    # TODO: используйте N + 1 узлов и оценку из пункта 4.
    pass

# Сравнение точностей поиска нулевой оценки.
assert score(0) < 0 < score(1)
for eps in (1e-2, 1e-3, 1e-4):
    left, right, steps = bisect_zero(score, 0.0, 1.0, eps)
    print(f"eps = {eps:g}; шагов: {steps}")
    print(f"Отрезок: [{left:.8f}, {right:.8f}]")
    print(f"Оценка погрешности t: {(right - left) / 2:.8f}")

# Концы и середина последнего найденного отрезка.
fig, axes = plt.subplots(1, 3, figsize=(10, 4.5))
for ax, t in zip(axes, [left, (left + right) / 2, right]):
    image = ((1 - t) * u + t * v).reshape(8, 8)
    ax.imshow(image, cmap="gray", vmin=0, vmax=1)
    ax.set_title(
        f"t = {t:.7f}\nF(t) = {score(t):.7f}\nОтвет: {answer(t)}",
        fontsize=10,
    )
    ax.axis("off")
fig.tight_layout()

# Гарантия для всех изображений на отрезке [0, 0.1].
for N in (2, 5, 10, 20):
    mu_grid, lower_bound, confirmed = check_interval(
        score, L, 0.0, 0.1, N
    )
    print(f"N = {N}; mu_h = {mu_grid:.6f}")
    print(f"Нижняя оценка mu: {lower_bound:.6f}")
    if confirmed:
        print(f"На всём отрезке подтверждён ответ: {answer(0)}")
    else:
        print("Полученной оценки недостаточно для гарантии.")
plt.show()
