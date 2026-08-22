import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression


# ============================================================
# 1. Black boxes
# ============================================================

def make_black_boxes():
    """
    Creates black boxes for the experiment.

    Hidden true boundaries:
    L_TRUE and R_TRUE are not returned.
    Students should not use them in the algorithm.
    """

    L_TRUE = -0.35
    R_TRUE = 1.20

    # We train a very simple sklearn model that returns the first coordinate.
    # The object has the form x = [target_score, side].
    rng = np.random.default_rng(42)

    target_scores = rng.uniform(-3.0, 3.0, size=1000)
    sides = rng.integers(0, 2, size=1000)

    X_train = np.column_stack([target_scores, sides])
    y_train_score = target_scores

    score_model = LinearRegression()
    score_model.fit(X_train, y_train_score)

    def make_probe(q, side):
        """
        Creates a probe object.

        q    -- desired score;
        side -- 0 for probing the right boundary of class 0;
                1 for probing the left boundary of class 1.
        """
        return np.array([[q, side]], dtype=float)

    def score_box(x):
        """Black box returning S(x)."""
        return float(score_model.predict(x)[0])

    def label_box(x):
        """
        Black box returning Y(x).

        For side = 0:
            y = 0 for scores <= L_TRUE,
            y = 1 for scores >  L_TRUE.

        For side = 1:
            y = 0 for scores <  R_TRUE,
            y = 1 for scores >= R_TRUE.
        """
        s = score_box(x)
        side = int(round(x[0, 1]))

        if side == 0:
            return int(s > L_TRUE)

        if side == 1:
            return int(s >= R_TRUE)

        raise ValueError("side must be 0 or 1")

    return make_probe, score_box, label_box


make_probe, score_box, label_box = make_black_boxes()


# ============================================================
# 2. TODO: implement bisection
# ============================================================

def bisect_boundary(make_probe, label_box, side, left, right, epsilon):
    """
    Finds a boundary by bisection.

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
# 3. Run the algorithm
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

print("Approximation of L:", L_star)
print("Final interval for L:", L_interval)

print()
print("Approximation of R:", R_star)
print("Final interval for R:", R_interval)

L_upper = L_interval[1]
R_lower = R_interval[0]

if L_upper < R_lower:
    threshold = 0.5 * (L_upper + R_lower)
    print()
    print("Certified separating threshold:", threshold)
else:
    threshold = 0.5 * (L_star + R_star)
    print()
    print("Intervals still overlap.")
    print("Try a smaller epsilon.")
    print("Candidate threshold:", threshold)


# ============================================================
# 4. Plot interval lengths
# ============================================================

L_lengths = [b - a for a, b in L_history]
R_lengths = [b - a for a, b in R_history]

plt.figure(figsize=(8, 5))
plt.semilogy(L_lengths, label="interval for L")
plt.semilogy(R_lengths, label="interval for R")
plt.xlabel("iteration")
plt.ylabel("interval length")
plt.title("Nested intervals shrink by bisection")
plt.legend()
plt.grid(True)
plt.show()


# ============================================================
# 5. Plot final localization on the score line
# ============================================================

plt.figure(figsize=(9, 2))

plt.axvspan(L_interval[0], L_interval[1], alpha=0.3, label="final interval for L")
plt.axvspan(R_interval[0], R_interval[1], alpha=0.3, label="final interval for R")
plt.axvline(threshold, linestyle="--", label="threshold")

plt.yticks([])
plt.xlabel("score")
plt.title("Localization of the unknown separating boundaries")
plt.legend()
plt.grid(True)
plt.show()
