"""
Функции, которые опирируют со словорями.
"""


# Шаг 15 (1)
def get_keys(dictionary):
    """Возвращает список ключей словаря."""
    return list(dictionary.keys())


# Шаг 15 (2)
def merge_dicts(*dicts):
    """Объединяет несколько словарей с приоритетом последних словарей."""
    merged_dict = {}
    for d in dicts:
        merged_dict.update(d)
    return merged_dict


# Шаг 15 (3)
def filter_dict(dictionary, threshold):
    """Фильтрует словарь, оставляя элементы со значениями выше порога."""
    return {k: v for k, v in dictionary.items() if v > threshold}


# Шаг 16
def count_key_occurrences(key, *dicts):
    """Подсчитывает, сколько словарей содержат указанный ключ."""
    return sum(1 for d in dicts if key in d)


# Шаг 17
def get_deep_value(dictionary, *keys):
    """
    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    Формулировка была не ясной — ищет значения по ключам на последнем уровне вложенности.
    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    """

    # Ищем самый глубокий уровень словаря
    while isinstance(dictionary, dict) and any(isinstance(v, dict) for v in dictionary.values()):
        # Переход на следующий уровень вложенности, если есть вложенные словари
        for value in dictionary.values():
            if isinstance(value, dict):
                dictionary = value
                break

    # Поиск значений по переданным ключам на самом глубоком уровне
    found_values = {key: dictionary[key] for key in keys if key in dictionary}
    return found_values if found_values else None
