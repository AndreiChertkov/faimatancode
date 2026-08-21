def sorting_hat(month):
    # TODO: реализуйте решающее дерево в исходном виде
    # через if/else, следуя вершинам на рисунке.
    pass

# TODO: реализуйте упрощённые предикаты факультетов.
def is_gryffindor(month):
    pass

def is_slytherin(month):
    pass

def is_ravenclaw(month):
    pass

def is_hufflepuff(month):
    pass

M = set(range(1, 13))

# Множества, полученные напрямую из решающего дерева.
from_tree = {
    "Гриф": {m for m in M if sorting_hat(m) == "Гриф"},
    "Слиз": {m for m in M if sorting_hat(m) == "Слиз"},
    "Когт": {m for m in M if sorting_hat(m) == "Когт"},
    "Пуфф": {m for m in M if sorting_hat(m) == "Пуфф"},
}

# Множества, полученные из упрощённых предикатов.
from_predicates = {
    "Гриф": {m for m in M if is_gryffindor(m)},
    "Слиз": {m for m in M if is_slytherin(m)},
    "Когт": {m for m in M if is_ravenclaw(m)},
    "Пуфф": {m for m in M if is_hufflepuff(m)},
}

for faculty in from_tree:
    print(faculty)
    print("  из дерева:    ", sorted(from_tree[faculty]))
    print("  из предиката: ", sorted(from_predicates[faculty]))
    print("  совпадает:    ", from_tree[faculty] == from_predicates[faculty])