"""
Функции, которые опирируют со списками.
"""

import random

# Шаг 1
def reverse_list(lst):
    """Переворачивает список."""
    return lst[::-1]


# Шаг 2
def modify_list(lst, values):
    """Изменяет значения списка в соответствии с переданными."""
    for i, value in enumerate(values):
        if i < len(lst):
            lst[i] = value
    return lst


# Шаг 3
def compare_lists(*lists):
    """Сравнивает несколько списков. Возвращает True, если все равны."""
    return all(lst == lists[0] for lst in lists)


# Шаг 4
def slice_list(lst, start=None, end=None, step=1):
    """Возвращает срез списка с заданным шагом."""
    return lst[start:end:step]


# Шаг 5
def create_list(*args):
    """Создаёт и возвращает список из переданных значений."""
    return list(args)


# Шаг 6
def insert_into_list(lst, index, value):
    """Вставляет элемент в указанную позицию списка."""
    lst.insert(index, value)
    return lst


# Шаг 7
def merge_and_sort_lists(*lists, reverse=False):
    """Объединяет и сортирует несколько списков."""
    merged_list = []
    for lst in lists:
        merged_list.extend(lst)
    return sorted(merged_list, reverse=reverse)


# Шаг 8
def random_list_operations():
    """Создаёт список случайной длины и проверяет его длину на чётность.
    Если нечётная, ищет центральный элемент и возвращает его количество в списке."""
    while True:
        lst = [random.randint(0, 10) for _ in range(random.randint(1, 20))]
        if len(lst) % 2 == 1:
            central_value = lst[len(lst) // 2]
            return lst.count(central_value)
        print(f"Список чётной длины: {lst}. Создаём новый список.")


# Шаг 9
def extend_list_with_limit(main_list, *other_lists, limit):
    """Расширяет основной список, ограничивая его длину заданным лимитом."""
    for lst in other_lists:
        main_list.extend(lst)
    if len(main_list) > limit:
        main_list = main_list[:limit]
    return main_list


# Шаг 9: функции сортировки (дополнительные функции)
def sort_by_length(lst):
    """Сортирует список по длине элементов (для списков строк)."""
    return sorted(lst, key=len)


def sort_by_last_digit(lst):
    """Сортирует список по последней цифре каждого элемента."""
    return sorted(lst, key=lambda x: int(str(x)[-1]))


def sort_descending(lst):
    """Сортирует список по убыванию."""
    return sorted(lst, reverse=True)


def sort_and_square(lst):
    """Сортирует список по значениям и возводит каждый элемент в квадрат."""
    return list(map(lambda x: x ** 2, sorted(lst)))


def sort_and_double(lst):
    """Сортирует список и удваивает каждый элемент."""
    return list(map(lambda x: x * 2, sorted(lst)))


def sort_absolute(lst):
    """Сортирует список по абсолютным значениям."""
    return sorted(lst, key=abs)


# Шаг 10
def extract_min(lst):
    """Извлекает и удаляет минимальный элемент из списка."""
    min_value = min(lst)
    lst.remove(min_value)
    return min_value
