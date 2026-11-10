import numpy as np
from sklearn.datasets import load_digits
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

# Подготовка данных и обучение экспертов.
images, digits = load_digits(return_X_y=True)
X = images / 16.0
y = digits % 2  # 0 -- чётная цифра, 1 -- нечётная.
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y
)

first = LogisticRegression(max_iter=500).fit(X_train, y_train)
second = KNeighborsClassifier(
    n_neighbors=5, algorithm="brute", n_jobs=1
).fit(X_train, y_train)

# Оценки первого эксперта и вес второго.
a = first.predict_proba(X_test)[:, 1]
g = 2 * np.abs(2 * a - 1)
w = np.maximum((1 - g) / 2, 0)

def predict(epsilon):
    """
    Возвращает итоговые оценки нечётности и число изображений,
    обработанных вторым экспертом при допуске epsilon.
    """
    # TODO: выберите по весам изображения для второго эксперта.
    # Вызовите second.predict_proba только для выбранных изображений
    # и вычислите на них ответ смеси. Для остальных оставьте ответ a.
    pass

# Сравнение с обычным sparsemax.
baseline, _ = predict(0.0)
baseline_labels = baseline >= 0.5

for epsilon in (0.0, 0.10, 0.20, 0.35):
    scores, count = predict(epsilon)
    labels = scores >= 0.5

    max_difference = np.max(np.abs(scores - baseline))
    accuracy = np.mean(labels == y_test)
    changed = np.count_nonzero(labels != baseline_labels)

    assert max_difference <= epsilon + 1e-12
    print(f"Допуск: {epsilon:.2f}")
    print(f"Изображений для второго эксперта: {count}")
    print(f"Максимальное отклонение: {max_difference:.4f}")
    print(f"Точность: {accuracy:.2%}. Изменилось меток: {changed}")
