# Определение числового объекта:
number = 120

# Определение функции, возвращающей числовое значение:
def last_digit(n):
    return n % 10

# Определение предиката, возвращающего True или False:
def has_last_digit_zero(n):
    return last_digit(n) == 0

# Алгебраическое выражение:
print(last_digit(number))        # «\cmo{1}»

# Логические выражения:
print(last_digit(number) == 0)   # «\cmo{2}»
print(last_digit(number) == 5)   # «\cmo{3}»

# Высказывания, получаемые из предиката:
print(has_last_digit_zero(120))  # «\cmo{4}»
print(has_last_digit_zero(123))  # «\cmo{5}»