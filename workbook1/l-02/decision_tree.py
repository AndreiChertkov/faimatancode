# Универсум входных значений
M = set(range(1, 13))

# Область прибытия с учётом ответа "Отчислен"
Y = {
    "Гриффиндор",
    "Когтевран",
    "Пуффендуй",
    "Слизерин",
    "Отчислен",
}

# Область прибытия только из факультетов
Y_fac = {
    "Гриффиндор",
    "Когтевран",
    "Пуффендуй",
    "Слизерин",
}

# Дерево задаём рекурсивно.
# Внутренняя вершина содержит predicate, true, false.
# Лист содержит value.
tree = {
    "name": "P1: x <= 6",
    "predicate": lambda x: x <= 6,
    "true": {
        "name": "P2: x <= 3",
        "predicate": lambda x: x <= 3,
        "true": {
            "name": "P4: x == 2",
            "predicate": lambda x: x == 2,
            "true": {"value": "Когтевран"},
            "false": {"value": "Гриффиндор"},
        },
        "false": {
            "name": "P5: x <= 2",
            "predicate": lambda x: x <= 2,
            "true": {"value": "Отчислен"},
            "false": {"value": "Пуффендуй"},
        },
    },
    "false": {
        "name": "P3: x <= 9",
        "predicate": lambda x: x <= 9,
        "true": {
            "name": "P6: x == 8",
            "predicate": lambda x: x == 8,
            "true": {"value": "Слизерин"},
            "false": {"value": "Гриффиндор"},
        },
        "false": {
            "name": "P7: x == 12",
            "predicate": lambda x: x == 12,
            "true": {"value": "Когтевран"},
            "false": {"value": "Пуффендуй"},
        },
    },
}

def predict(tree, x):
    """Возвращает значение решающего дерева на входе x."""
    if "value" in tree:
        return tree["value"]

    if tree["predicate"](x):
        return predict(tree["true"], x)
    else:
        return predict(tree["false"], x)

def leaf_values(tree):
    """
    Возвращает список значений, записанных в листьях дерева.
    Если два листа имеют одно и то же значение, оно будет в списке дважды.
    """
    if "value" in tree:
        return [tree["value"]]

    return leaf_values(tree["true"]) + leaf_values(tree["false"])

# TODO: реализуйте необходимые условия.

def necessary_for_injective(X, Y, leaves):
    """
    Верните True, если выполнены выбранные вами необходимые условия
    для того, чтобы функция X -> Y могла быть инъективной.
    """
    pass

def necessary_for_surjective(X, Y, leaves):
    """
    Верните True, если выполнены выбранные вами необходимые условия
    для того, чтобы функция X -> Y могла быть сюръективной.
    """
    pass

def necessary_for_bijective(X, Y, leaves):
    """
    Верните True, если выполнены выбранные вами необходимые условия
    для того, чтобы функция X -> Y могла быть биективной.
    """
    pass

# Вспомогательные функции для фактической проверки свойств на конечном M.
# Их можно использовать, чтобы найти пример: необходимые условия выполнены,
# но функция всё равно не принадлежит нужному классу.

def image(tree, X):
    return {predict(tree, x) for x in X}

def is_injective_on_universe(tree, X):
    outputs = [predict(tree, x) for x in X]
    return len(outputs) == len(set(outputs))

def is_surjective_on_universe(tree, X, Y):
    return image(tree, X) == set(Y)

def is_bijective_on_universe(tree, X, Y):
    return is_injective_on_universe(tree, X) and is_surjective_on_universe(tree, X, Y)

leaves = leaf_values(tree)
print("Листья дерева:", leaves)
print("Значения на M:", {x: predict(tree, x) for x in sorted(M)})

print("Необходимые условия для инъективности:", necessary_for_injective(M, Y, leaves))
print("Необходимые условия для сюръективности:", necessary_for_surjective(M, Y, leaves))
print("Необходимые условия для биективности:", necessary_for_bijective(M, Y, leaves))

print("Фактически инъекция:", is_injective_on_universe(tree, M))
print("Фактически сюръекция на Y:", is_surjective_on_universe(tree, M, Y))
print("Фактически биекция:", is_bijective_on_universe(tree, M, Y))