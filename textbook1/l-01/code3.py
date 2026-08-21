# Проверка ∀ x ∈ X : P(x)
def forall(X, P):
    return all(P(x) for x in X)

# Проверка ∃ x ∈ X : P(x)
def exists(X, P):
    return any(P(x) for x in X)

# Проверка ∃! x ∈ X : P(x)
def existsu(X, P):
    return sum(1 for x in X if P(x)) == 1

# Универсум:
X = list(range(-3, 4))

# Предикаты:
def P(x): return x * x >= 0   # P(x) :⇔ x^2 >= 0
def Q(x): return x > 0        # Q(x) :⇔ x > 0
def R(x): return x == 0       # R(x) :⇔ x = 0

# Базовые кванторные высказывания:
print("∀  x ∈ X : x^2 >= 0 ->", forall(X, P))   # «\cmo{1}»
print("∃  x ∈ X : x    > 0 ->", exists(X, Q))   # «\cmo{2}»
print("∃! x ∈ X : x    = 0 ->", existsu(X, R))  # «\cmo{3}»