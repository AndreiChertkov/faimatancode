def product(X, Y):          # Прямое произведение
    return {(x, y) for x in X for y in Y}

def is_function(f):         # Проверка, что f — функция
    return len(f) == len(domain(f))

def domain(f):              # Область определения
    return {x for (x, _) in f}

def values(f):              # Множество значений
    return {y for (_, y) in f}

def apply(f, x):            # Действие функции на аргумент
    for (a, y) in f:
        if a == x:
            return y
    raise ValueError(f"Функция не определена в точке {x}")

def image(f, A):            # Образ подмножества
    return {y for (x, y) in f if x in A}

def preimage(f, B):         # Прообраз подмножества
    return {x for (x, y) in f if y in B}

def restrict(f, A):         # Сужение функции на подмножество
    return {(x, y) for (x, y) in f if x in A}

def is_surjection(f, Y):    # Проверка, что f — сюръекция
    return is_function(f) and values(f) == Y

def is_injection(f):        # Проверка, что f — инъекция
    return is_function(f) and len(f) == len(values(f))

def is_bijection(f, Y):     # Проверка, что f — биекция
    return is_surjection(f, Y) and is_injection(f)

def inverse(f):             # Обратная функция
    if not is_injection(f):
        raise ValueError("Обратная функция не определена")
    return {(y, x) for (x, y) in f}

P = {"Анна", "Борис", "Вера", "Глеб", "Дима", "Лектор"}
S = {"Анна", "Борис", "Вера", "Глеб", "Дима"}
T = {"t1", "t2", "t3", "t4"}

table_by_student = {"Анна": "t1", "Борис": "t1",
    "Вера": "t2", "Глеб": "t3", "Дима": "t3"}

f = set(table_by_student.items())

# Функция — подмножество прямого произведения:
print("f ⊂ P × T:", f <= product(P, T))           # «\cmo{1}»
print("f является функцией:", is_function(f))     # «\cmo{2}»

# Область определения и множество значений:
print("X_f =", sorted(domain(f)))                 # «\cmo{3}»
print("Y_f =", sorted(values(f)))                 # «\cmo{4}»

# Применение функции:
print("f(Вера) =", apply(f, "Вера"))              # «\cmo{5}»

# Образ подмножества f(A):
A = {"Анна", "Вера"}
print("f(A) =", sorted(image(f, A)))              # «\cmo{6}»

# Прообраз подмножества f^{-1}(B):
B = {"t1", "t2"}
print("f^{-1}(B) =", sorted(preimage(f, B)))      # «\cmo{7}»

# Свойства исходной функции f:
print("f сюръекция :", is_surjection(f, T))       # «\cmo{8}»
print("f инъекция  :", is_injection(f))           # «\cmo{9}»
print("f биекция   :", is_bijection(f, T))        # «\cmo{10}»

# Сужение функции:
C = {"Анна", "Вера", "Глеб"}
f_C = restrict(f, C)
Y_C = values(f_C)

# Свойства новой функции f_C:
print("f|_C сюръекция :", is_surjection(f_C, Y_C)) # «\cmo{11}»
print("f|_C инъекция  :", is_injection(f_C))       # «\cmo{12}»
print("f|_C биекция   :", is_bijection(f_C, Y_C))  # «\cmo{13}»

# Построение обратной функции и её применение:
f_C_inverse = inverse(f_C)
print("(f|_C)^{-1}(t2) =", apply(f_C_inverse, "t2")) # «\cmo{14}»