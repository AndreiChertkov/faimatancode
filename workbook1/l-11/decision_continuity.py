from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPRegressor

# Подготовка данных и обучение небольшой сети.
images, digits = load_digits(return_X_y=True)
mask = np.isin(digits, [3, 8])
X = images[mask] / 16.0
y = np.where(digits[mask] == 3, -1.0, 1.0)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y
)
network = MLPRegressor(
    hidden_layer_sizes=(16,), activation="relu", solver="lbfgs",
    alpha=1e-3, max_iter=2000, random_state=42,
).fit(X_train, y_train)

# Выбираем по одному правильно распознанному изображению.
predictions = network.predict(X_test)
threes = np.flatnonzero((y_test == -1) & (predictions < 0))
eights = np.flatnonzero((y_test == 1) & (predictions > 0))
if len(threes) == 0 or len(eights) == 0:
    raise RuntimeError("Не найдена подходящая пара изображений.")
u, v = X_test[threes[0]], X_test[eights[0]]

# Коэффициенты F(t) = d + sum(c_j * ReLU(a_j * t + b_j)).
weights = network.coefs_[0]
a = (v - u) @ weights
b = u @ weights + network.intercepts_[0]
c = network.coefs_[1][:, 0]
d = float(network.intercepts_[1][0])

def score(t):
    """Числовая оценка F(t) смеси двух изображений."""
    # TODO: вычислите оценку по коэффициентам a, b, c, d.
    pass

def answer(t):
    """Ответ 3 или 8; при нулевой оценке выбираем 8."""
    # TODO: используйте score(t).
    pass

def sensitivity_bound():
    """Верхняя оценка L изменения выхода сети."""
    # TODO: вычислите L по коэффициентам a и c.
    pass

L = sensitivity_bound()
rho = abs(score(0)) / L if L > 0 else float("inf")
print(f"F(0) = {score(0):.6f}; F(1) = {score(1):.6f}")
print(f"L = {L:.6f}; радиус rho(0) = {rho:.6f}")

# Сохраняем тот же пример для практики 12.
data_path = Path(__file__).with_name("digits_path.npz")
np.savez(data_path, a=a, b=b, c=c, d=d, u=u, v=v, L=L)
print(f"Сохранено: {data_path}")

# Графики оценки и ответа вдоль перехода.
ts = np.linspace(0, 1, 101)
scores = np.array([score(t) for t in ts])
answers = np.array([answer(t) for t in ts])
fig, axes = plt.subplots(2, 1, figsize=(9, 6), sharex=True)
axes[0].plot(ts, scores)
axes[0].axhline(0, color="gray", linestyle="--")
axes[0].set(ylabel="F(t)", title="Оценка изображения")
axes[1].step(ts, answers, where="post")
axes[1].set(xlabel="t", ylabel="Y(t)", yticks=[3, 8])
for ax in axes:
    ax.axvspan(0, min(rho, 1), color="green", alpha=0.15)
    ax.grid(True)
fig.tight_layout()

# Промежуточные изображения.
fig, axes = plt.subplots(1, 5, figsize=(12, 3.5))
for ax, t in zip(axes, np.linspace(0, 1, 5)):
    image = ((1 - t) * u + t * v).reshape(8, 8)
    ax.imshow(image, cmap="gray", vmin=0, vmax=1)
    ax.set_title(f"t = {t:.2f}\nОтвет: {answer(t)}", fontsize=10)
    ax.axis("off")
fig.tight_layout()
plt.show()
