"""
Демонстрация работы с функциями, которые обрабатывают списки, кортежи и словари.
"""

from list_operations import (
    reverse_list, modify_list, compare_lists, slice_list, create_list,
    insert_into_list, merge_and_sort_lists, random_list_operations,
    extend_list_with_limit, extract_min, sort_by_length, sort_by_last_digit,
    sort_descending, sort_and_square, sort_and_double, sort_absolute
)
from tuple_operations import (
    concatenate_tuples, find_common_elements, types_tuple, element_in_tuple
)
from dict_operations import (
    get_keys, merge_dicts, filter_dict, count_key_occurrences, get_deep_value
)


def main():
    """
    Главная функция для тестирования операций над списками, кортежами и словарями.
    Демонстрирует применение каждой функции с тестовыми данными и выводит результат.
    """
    # Примеры работы с функциями списка
    print(reverse_list([1, 2, 3]))  # Шаг 1
    print(modify_list([1, 2, 3], [9, 8, 7]))  # Шаг 2
    print(compare_lists([1, 2, 3], [1, 2, 3], [1, 2, 3]))  # Шаг 3
    print(slice_list([1, 2, 3, 4, 5], 1, 4, 2))  # Шаг 4
    print(create_list(1, 2, 3))  # Шаг 5
    print(insert_into_list([1, 2, 3], 1, 9))  # Шаг 6
    print(merge_and_sort_lists([1, 2], [3, 4], reverse=True))  # Шаг 7
    print(random_list_operations())  # Шаг 8
    print(extend_list_with_limit([1, 2], [3, 4, 5], limit=4))  # Шаг 9
    print(extract_min([4, 2, 3, 1]))  # Шаг 10

    # Сортировка (шаг 9)
    print(sort_by_length(["apple", "kiwi", "banana"]))
    print(sort_by_last_digit([34, 25, 46, 57]))
    print(sort_descending([1, 2, 3]))
    print(sort_and_square([1, -2, 3]))
    print(sort_and_double([1, 2, 3]))
    print(sort_absolute([-10, 3, 7, -4]))

    # Примеры работы с кортежами
    print(concatenate_tuples((1, 2), (3, 4)))  # Шаг 11 (1)
    print(find_common_elements((1, 2, 3), (2, 3, 4), (3, 4, 5)))  # Шаг 11 (2)
    print(types_tuple(1, 'a', 3.14))  # Шаг 12
    print(element_in_tuple((1, 2, 3), 2))  # Шаг 13

    # Примеры работы со словарями
    dictionary = {'a': 1, 'b': 2, 'c': 3}
    print(get_keys(dictionary))  # Шаг 15 (1)
    print(merge_dicts({'a': 1}, {'b': 2}))  # Шаг 15 (2)
    print(filter_dict(dictionary, 1))  # Шаг 15 (3)
    print(count_key_occurrences('a', {'a': 1}, {'a': 2}, {'b': 3}))  # Шаг 16
    print(get_deep_value({'a': {'b': {'c': 5, 'd': 6, 'e': 7}}}, 'a', 'c', 'e'))  # Шаг 17


if __name__ == "__main__":
    main()
