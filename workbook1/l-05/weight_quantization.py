import matplotlib.pyplot as plt
import numpy as np

from sklearn.datasets import load_diabetes
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

W_MIN = -200
W_MAX = 200

# ============================================================
# Данные: load_diabetes, один признак, без свободного члена
# ============================================================

data = load_diabetes()

feature_names = list(data.feature_names)
feature_index = feature_names.index("bmi")

X = data.data[:, [feature_index]]
y = data.target.astype(float)

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.3,
    random_state=42,
)

scaler = StandardScaler()

x_train = scaler.fit_transform(X_train).ravel()
x_test = scaler.transform(X_test).ravel()

y_mean = y_train.mean()

y_train_centered = y_train - y_mean
y_test_centered = y_test - y_mean

model = LinearRegression(fit_intercept=False)
model.fit(x_train.reshape(-1, 1), y_train_centered)

w_cont = float(model.coef_[0])

print("Оптимальный непрерывный вес:", w_cont)


def mse_for_weight(w, x, y):
    """
    Возвращает MSE модели f_w(x) = w x.

    Параметры:
    w -- вес модели;
    x -- массив признаков;
    y -- массив ответов.

    Возвращает:
    среднеквадратичную ошибку.
    """
    # TODO: реализуйте подсчёт MSE
    pass


continuous_train_mse = mse_for_weight(
    w_cont,
    x_train,
    y_train_centered,
)

continuous_test_mse = mse_for_weight(
    w_cont,
    x_test,
    y_test_centered,
)

print("Train MSE непрерывной модели:", continuous_train_mse)
print("Test MSE непрерывной модели:", continuous_test_mse)


def make_uniform_grid(w_min, w_max, h):
    """
    Строит равномерную сетку весов на отрезке [w_min, w_max] с шагом h.

    Возвращает:
    numpy-массив допустимых весов.
    """
    # TODO: реализуйте построение сетки
    pass


def quantize_to_grid(w, grid):
    """
    Округляет число w до ближайшего элемента сетки grid.

    Параметры:
    w    -- число, которое нужно квантизовать;
    grid -- массив допустимых значений.

    Возвращает:
    ближайший к w элемент сетки.
    """
    # TODO: найдите элемент grid, ближайший к w
    pass


def evaluate_quantized_model(
    w_cont,
    h,
    x_train,
    y_train,
    x_test,
    y_test,
    continuous_train_mse,
    continuous_test_mse,
    w_min=W_MIN,
    w_max=W_MAX,
):
    """
    Оценивает ошибку модели после квантизации оптимального веса.

    Возвращает:
    q              -- квантизованный вес;
    train_mse_q    -- train MSE квантизованной модели;
    test_mse_q     -- test MSE квантизованной модели;
    train_increase -- увеличение train MSE;
    test_increase  -- увеличение test MSE.
    """
    # TODO: построить сетку
    # TODO: найти q
    # TODO: посчитать train и test MSE
    # TODO: посчитать увеличение ошибки
    pass


def best_weight_on_grid(grid, x_train, y_train):
    """
    Находит вес q из сетки grid, минимизирующий train MSE.

    Возвращает:
    best_q         -- лучший вес на сетке;
    best_train_mse -- train MSE для этого веса.
    """
    # TODO: переберите все q из grid
    # TODO: посчитайте MSE для каждого q
    # TODO: выберите q с минимальным MSE
    pass


def make_custom_grid(
    w_min,
    w_max,
    w_center,
    radius,
    num_global,
    num_local,
):
    """
    Строит неравномерную сетку.

    Идея:
    - грубая глобальная сетка покрывает весь отрезок [w_min, w_max];
    - более плотная локальная сетка строится около w_center.

    Параметры:
    w_center   -- центр локальной сетки;
    radius     -- радиус локальной области;
    num_global -- число точек глобальной сетки;
    num_local  -- число точек локальной сетки.

    Возвращает:
    numpy-массив узлов неравномерной сетки.
    """
    # TODO: построить глобальную сетку
    # TODO: построить локальную сетку
    # TODO: объединить их и удалить повторы
    pass


h_values = np.array([
    50,
    20,
    10,
    5,
    2,
    1,
    0.5,
    0.2,
    0.1,
], dtype=float)

quantized_train_mse = []
quantized_test_mse = []
quantized_weights = []

grid_best_train_mse = []
grid_best_test_mse = []
grid_best_weights = []

for h in h_values:
    grid = make_uniform_grid(W_MIN, W_MAX, h)

    q = quantize_to_grid(w_cont, grid)

    train_mse_q = mse_for_weight(q, x_train, y_train_centered)
    test_mse_q = mse_for_weight(q, x_test, y_test_centered)

    best_q, best_train_mse = best_weight_on_grid(
        grid,
        x_train,
        y_train_centered,
    )

    best_test_mse = mse_for_weight(
        best_q,
        x_test,
        y_test_centered,
    )

    quantized_weights.append(q)
    quantized_train_mse.append(train_mse_q)
    quantized_test_mse.append(test_mse_q)

    grid_best_weights.append(best_q)
    grid_best_train_mse.append(best_train_mse)
    grid_best_test_mse.append(best_test_mse)

    print()
    print("h =", h)
    print("q = Q_h(w_cont):", q)
    print("best q on grid:", best_q)
    print("continuous train MSE:", continuous_train_mse)
    print("quantized train MSE:", train_mse_q)
    print("grid best train MSE:", best_train_mse)

plt.figure(figsize=(8, 5))

plt.plot(
    h_values,
    quantized_train_mse,
    marker="o",
    label="train MSE after quantization",
)

plt.plot(
    h_values,
    grid_best_train_mse,
    marker="o",
    label="best train MSE on grid",
)

plt.axhline(
    continuous_train_mse,
    linestyle="--",
    label="continuous train MSE",
)

plt.xscale("log")
plt.gca().invert_xaxis()
plt.xlabel("Шаг сетки h")
plt.ylabel("Train MSE")
plt.title("Ошибка регрессии при квантизации веса")
plt.legend()
plt.grid(True)
plt.show()

plt.figure(figsize=(8, 5))

plt.plot(
    h_values,
    quantized_test_mse,
    marker="o",
    label="test MSE after quantization",
)

plt.plot(
    h_values,
    grid_best_test_mse,
    marker="o",
    label="test MSE for best grid weight",
)

plt.axhline(
    continuous_test_mse,
    linestyle="--",
    label="continuous test MSE",
)

plt.xscale("log")
plt.gca().invert_xaxis()
plt.xlabel("Шаг сетки h")
plt.ylabel("Test MSE")
plt.title("Test MSE при квантизации веса")
plt.legend()
plt.grid(True)
plt.show()
