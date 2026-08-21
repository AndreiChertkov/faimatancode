import matplotlib.pyplot as plt
import numpy as np

rng = np.random.default_rng(42)

class0 = rng.normal(loc=[-2, 0], scale=0.6, size=(40, 2))
class1 = rng.normal(loc=[2, 0], scale=0.6, size=(40, 2))

X = np.vstack([class0, class1])
y = np.array([0] * len(class0) + [1] * len(class1))

w = np.array([1.0, 0.0])
scores = X @ w

a = scores[y == 0].max()
b = scores[y == 1].min()

print("a =", a)
print("b =", b)
print("separable:", a < b)


def bisect_interval(a, b, eps):
    """
    Метод бисекции для локализации порога t_* = (a + b) / 2.
    Возвращает список промежуточных отрезков и найденное приближение.
    """
    # TODO: реализуйте метод бисекции.
    pass


def predict_by_threshold(X, w, t):
    """Классификатор F_t(x) = 1, если <w, x> >= t, иначе 0."""
    # TODO: реализуйте классификацию по порогу.
    pass


eps = 1e-3
intervals, t_hat = bisect_interval(a, b, eps)

print("threshold:", t_hat)
print("last interval length:", intervals[-1][1] - intervals[-1][0])

pred = predict_by_threshold(X, w, t_hat)
accuracy = np.mean(pred == y)

print("accuracy:", accuracy)

plt.figure(figsize=(7, 5))

plt.scatter(class0[:, 0], class0[:, 1], label="class 0")
plt.scatter(class1[:, 0], class1[:, 1], label="class 1")

plt.axvline(t_hat, linestyle="--", label="separating line")

plt.legend()
plt.title("Separating line found by bisection")
plt.grid(True)
plt.show()

lengths = [right - left for left, right, c in intervals]
steps = list(range(len(lengths)))

plt.figure(figsize=(8, 5))
plt.plot(steps, lengths, marker="o")
plt.xlabel("step")
plt.ylabel("interval length")
plt.title("Nested intervals in bisection")
plt.grid(True)
plt.show()
