"""
Функции, которые опирируют с кортежами.
"""

# Шаг 11 (1)
def concatenate_tuples(*tuples):
    """Объединяет несколько кортежей в один."""
    result = ()
    for tup in tuples:
        result += tup
    return result


# Шаг 11 (2)
def find_common_elements(*tuples):
    """Находит общие элементы в нескольких кортежах и возвращает их."""
    common_elements = set(tuples[0])
    for tup in tuples[1:]:
        common_elements &= set(tup)
    return common_elements


# Шаг 12
def types_tuple(*values):
    """Возвращает кортеж типов данных элементов входного кортежа."""
    return tuple(type(value) for value in values)


# Шаг 13
def element_in_tuple(tup, element):
    """Проверяет, существует ли элемент в кортеже."""
    return element in tup
