import numpy as np
import matplotlib.pyplot as plt

from math import ceil, log2, comb
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# ============================================================
# ДАННЫЕ: Wine из sklearn, но берём только часть признаков
# ============================================================

data = load_wine()

X_full = data.data
y = data.target
feature_names = list(data.feature_names)

selected_features = [
    "alcohol",
    "malic_acid",
    "alcalinity_of_ash",
    "flavanoids",
    "color_intensity",
]

selected_indices = [
    feature_names.index(name)
    for name in selected_features
]

X = X_full[:, selected_indices]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.3,
    random_state=42,
    stratify=y,
)

n_train = len(X_train)
p = X_train.shape[1]

print("Датасет: Wine")
print("Используемые признаки:", selected_features)
print("Размер train:", n_train)
print("Размер test:", len(X_test))
print("Число признаков p:", p)
print("Классы:", data.target_names)

# ============================================================
# ЗАДАЧА 1. Глубина дерева и переобучение
# ============================================================

def train_and_eval(d):
    """
    Обучает решающее дерево глубины d.
    Возвращает:
    train_accuracy, test_accuracy
    """
    model = DecisionTreeClassifier(
        max_depth=d,
        random_state=42,
    )

    model.fit(X_train, y_train)

    train_pred = model.predict(X_train)
    test_pred = model.predict(X_test)

    train_acc = accuracy_score(y_train, train_pred)
    test_acc = accuracy_score(y_test, test_pred)

    return train_acc, test_acc

def max_depth_bound(n):
    """
    Нужно реализовать самостоятельно.

    Подсказка:
    полное бинарное дерево глубины d имеет 2^d листьев.
    Нужно найти минимальное d, такое что 2^d >= n.
    """
    # TODO: замените на свою реализацию
    return ceil(log2(n))

depth_limit = max_depth_bound(n_train)

depths = list(range(1, depth_limit + 1))
tree_train_scores = []
tree_test_scores = []

for d in depths:
    train_acc, test_acc = train_and_eval(d)
    tree_train_scores.append(train_acc)
    tree_test_scores.append(test_acc)

best_index = int(np.argmax(tree_test_scores))
best_depth = depths[best_index]
best_test_accuracy = tree_test_scores[best_index]

print("Предельная глубина:", depth_limit)
print("Лучшая глубина по test accuracy:", best_depth)
print("Лучшее test accuracy:", best_test_accuracy)

plt.figure(figsize=(8, 5))
plt.plot(depths, tree_train_scores, marker="o", label="train accuracy")
plt.plot(depths, tree_test_scores, marker="o", label="test accuracy")
plt.xlabel("Глубина дерева")
plt.ylabel("Accuracy")
plt.title("Решающее дерево на Wine: зависимость качества от глубины")
plt.legend()
plt.grid(True)
plt.show()

# ============================================================
# ЗАДАЧА 2. Случайный лес без bootstrap
# ============================================================

# Для каждого набора параметров будем обучать несколько лесов
# и усреднять качество. Это уменьшает влияние случайности.
SEEDS = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def max_reasonable_T(p, r, d):
    """
    Нужно реализовать самостоятельно.

    Теоретическая верхняя граница:
    T_max = C(p, r)^(2^d - 1).
    """
    # TODO: замените на свою реализацию
    return comb(p, r) ** (2 ** d - 1)

def train_and_eval_forest_once(d, T, r, seed):
    """
    Обучает один случайный лес с фиксированным seed.
    Возвращает train_accuracy, test_accuracy.
    """
    model = RandomForestClassifier(
        n_estimators=T,
        max_depth=d,
        max_features=r,
        bootstrap=False,
        random_state=seed,
    )

    model.fit(X_train, y_train)

    train_pred = model.predict(X_train)
    test_pred = model.predict(X_test)

    train_acc = accuracy_score(y_train, train_pred)
    test_acc = accuracy_score(y_test, test_pred)

    return train_acc, test_acc

def train_and_eval_forest(d, T, r, seeds=SEEDS):
    """
    Обучает несколько случайных лесов с разными seed
    и возвращает средние значения качества.

    Возвращает:
    mean_train_accuracy, mean_test_accuracy
    """
    train_scores = []
    test_scores = []

    for seed in seeds:
        train_acc, test_acc = train_and_eval_forest_once(
            d=d,
            T=T,
            r=r,
            seed=seed,
        )
        train_scores.append(train_acc)
        test_scores.append(test_acc)

    mean_train_acc = float(np.mean(train_scores))
    mean_test_acc = float(np.mean(test_scores))

    return mean_train_acc, mean_test_acc

# Используем лучшую глубину из эксперимента с одним деревом.
d_opt = best_depth

r_values = sorted(set([
    1,
    2,
    p,
]))

print("Оптимальная глубина d из эксперимента с одним деревом:", d_opt)
print("Значения r:", r_values)
print("Сиды:", SEEDS)

T_EXPERIMENT_CAP = 100

forest_results = {}

for r in r_values:
    T_theory = max_reasonable_T(p, r, d_opt)
    T_limit = min(T_theory, T_EXPERIMENT_CAP)

    T_values = list(range(1, T_limit + 1))

    train_scores = []
    test_scores = []

    for T in T_values:
        mean_train_acc, mean_test_acc = train_and_eval_forest(
            d=d_opt,
            T=T,
            r=r,
            seeds=SEEDS,
        )

        train_scores.append(mean_train_acc)
        test_scores.append(mean_test_acc)

    forest_results[r] = {
        "T_theory": T_theory,
        "T_values": T_values,
        "train_scores": train_scores,
        "test_scores": test_scores,
    }

    print()
    print("r =", r)
    print("Теоретический T_max =", T_theory)
    print("В эксперименте использовали T до", T_limit)
    print("Лучшее среднее test accuracy =", max(test_scores))

for r in r_values:
    result = forest_results[r]

    plt.figure(figsize=(8, 5))

    plt.plot(
        result["T_values"],
        result["train_scores"],
        label="mean train accuracy",
    )

    plt.plot(
        result["T_values"],
        result["test_scores"],
        label="mean test accuracy",
    )

    plt.xlabel("Число деревьев T")
    plt.ylabel("Accuracy")
    plt.title(f"Случайный лес на Wine: d={d_opt}, r={r}")
    plt.legend()
    plt.grid(True)
    plt.show()