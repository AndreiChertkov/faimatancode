import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

# ============================================================
# 1. Чёрные ящики
# ============================================================

def make_black_boxes():
    """
    Создаёт чёрные ящики для эксперимента.

    Границы скрыты; L_TRUE и R_TRUE не возвращаются
    и не должны использоваться в алгоритме.
    """

    L_TRUE = -0.35
    R_TRUE = 1.20

    # Обучаем простую модель sklearn,
    # возвращающую первую координату.
    # Объект имеет вид x = [target_score, side].
    rng = np.random.default_rng(42)

    target_scores = rng.uniform(-3.0, 3.0, size=1000)
    sides = rng.integers(0, 2, size=1000)

    X_train = np.column_stack([target_scores, sides])
    y_train_score = target_scores

    score_model = LinearRegression()
    score_model.fit(X_train, y_train_score)

    def make_probe(q, side):
        """
        Создаёт зондирующий объект.

        q    -- желаемая числовая оценка;
        side -- 0 для поиска правой границы класса 0;
                1 для поиска левой границы класса 1.
        """
        return np.array([[q, side]], dtype=float)

    def score_box(x):
        """Чёрный ящик, возвращающий числовую оценку S(x)."""
        return float(score_model.predict(x)[0])

    def label_box(x):
        """
        Чёрный ящик, возвращающий класс Y(x).

        Для side = 0:
            класс 0, если оценка <= L_TRUE;
            класс 1, если оценка > L_TRUE.

        Для side = 1:
            класс 0, если оценка < R_TRUE;
            класс 1, если оценка >= R_TRUE.
        """
        s = score_box(x)
        side = int(round(x[0, 1]))

        if side == 0:
            return int(s > L_TRUE)

        if side == 1:
            return int(s >= R_TRUE)

        raise ValueError("Параметр side должен быть 0 или 1")

    return make_probe, score_box, label_box

make_probe, score_box, label_box = make_black_boxes()

# ============================================================
# 2. Задание: реализовать метод половинного деления
# ============================================================

def bisect_boundary(make_probe, label_box, side, left, right, epsilon):
    """
    Находит границу методом половинного деления.

    Параметры:
    make_probe -- функция создания probe-объектов;
    label_box  -- чёрный ящик меток;
    side       -- 0 для границы L, 1 для границы R;
    left       -- левый конец начального отрезка;
    right      -- правый конец начального отрезка;
    epsilon    -- требуемая точность.

    Предположение:
    label_box(make_probe(left, side)) == 0
    label_box(make_probe(right, side)) == 1

    Возвращает:
    boundary_star -- середина финального отрезка;
    interval      -- финальный отрезок [left, right];
    history       -- список всех промежуточных отрезков.
    """

    # TODO: проверьте корректность начального отрезка

    # TODO: создайте список history

    # TODO:
    # пока длина отрезка больше 2 * epsilon:
    #     возьмите середину;
    #     запросите метку у label_box;
    #     если метка 0, сдвиньте левый конец;
    #     если метка 1, сдвиньте правый конец.

    pass

# ============================================================
# 3. Запуск алгоритма
# ============================================================

epsilon = 1e-3

L_star, L_interval, L_history = bisect_boundary(
    make_probe=make_probe,
    label_box=label_box,
    side=0,
    left=-2.0,
    right=2.0,
    epsilon=epsilon,
)

R_star, R_interval, R_history = bisect_boundary(
    make_probe=make_probe,
    label_box=label_box,
    side=1,
    left=-2.0,
    right=2.0,
    epsilon=epsilon,
)

print("Приближение границы L:", L_star)
print("Финальный отрезок для L:", L_interval)
print()
print("Приближение границы R:", R_star)
print("Финальный отрезок для R:", R_interval)

L_upper = L_interval[1]
R_lower = R_interval[0]

if L_upper < R_lower:
    threshold = 0.5 * (L_upper + R_lower)
    print()
    print("Гарантированно разделяющий порог:", threshold)
else:
    threshold = 0.5 * (L_star + R_star)
    print()
    print("Отрезки пока перекрываются.")
    print("Попробуйте уменьшить epsilon.")
    print("Предполагаемый разделяющий порог:", threshold)

# ============================================================
# 4. Plot interval lengths
# ============================================================

L_lengths = [b - a for a, b in L_history]
R_lengths = [b - a for a, b in R_history]

plt.figure(figsize=(8, 5))
plt.semilogy(L_lengths, label="отрезок для L")
plt.semilogy(R_lengths, label="отрезок для R")
plt.xlabel("Номер итерации")
plt.ylabel("Длина отрезка")
plt.title("Вложенные отрезки при половинном делении")
plt.legend()
plt.grid(True)
plt.show()

# ============================================================
# 5. Финальная локализация на прямой числовых оценок
# ============================================================

plt.figure(figsize=(9, 2))
plt.axvspan(L_interval[0], L_interval[1], alpha=0.3,
    label="финальный отрезок для L")
plt.axvspan(R_interval[0], R_interval[1], alpha=0.3,
    label="финальный отрезок для R")
plt.axvline(threshold, linestyle="--", label="порог")
plt.yticks([])
plt.xlabel("Числовая оценка")
plt.title("Локализация неизвестных границ разделения")
plt.legend()
plt.grid(True)
plt.show()