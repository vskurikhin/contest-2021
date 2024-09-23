#!/usr/bin/env python3
import random
from typing import Callable
from typing import TypeVar

TV = TypeVar('TV')


def counting_sort(array: list[int], k: int):
    counted_values = [0] * k
    for value in array:
        counted_values[value] += 1

    index = 0
    for value in range(k):
        for amount in range(counted_values[value]):
            array[index] = value
            index += 1
    return array


def merge_sort(array: list[TV]) -> list[TV]:
    if len(array) == 1:  # базовый случай рекурсии
        return array

    # запускаем сортировку рекурсивно на левой половине
    left = merge_sort(array[0: len(array) // 2])

    # запускаем сортировку рекурсивно на правой половине
    right = merge_sort(array[len(array) // 2: len(array)])

    # заводим массив для результата сортировки
    result = [0] * len(array)

    # сливаем результаты
    l, r, k = 0, 0, 0
    while l < len(left) and r < len(right):
        # выбираем, из какого массива забрать минимальный элемент
        if left[l] <= right[r]:
            result[k] = left[l]
            l += 1
        else:
            result[k] = right[r]
            r += 1
        k += 1

    # Если один массив закончился раньше, чем второй, то
    # переносим оставшиеся элементы второго массива в результирующий
    while l < len(left):
        result[k] = left[l]  # перенеси оставшиеся элементы left в result
        l += 1
        k += 1
    while r < len(right):
        result[k] = right[r]  # перенеси оставшиеся элементы right в result
        r += 1
        k += 1

    return result


def swap(a: list[TV], i: int, j: int):
    temp = a[i]
    a[i] = a[j]
    a[j] = temp


# Раздел # с использованием схемы разделов Lomuto
def partition(a: list[TV], start: int, end: int):
    # Выберите крайний правый элемент в качестве опорного элемента из списка.
    pivot = a[end]

    # Элементы #, меньшие, чем точка поворота, будут перемещены влево от `p_index`
    # Элементы # больше, чем точка поворота, будут перемещены вправо от `p_index`
    # равные элементы могут идти в любом направлении
    p_index = start

    # каждый раз, когда мы находим элемент, меньший или равный опорному,
    # `p_index` увеличивается, и этот элемент будет помещен
    # перед разворотом.
    for i in range(start, end):
        if a[i] <= pivot:
            swap(a, i, p_index)
            p_index = p_index + 1

    # поменять `p_index` на пивот
    swap(a, end, p_index)

    # возвращает `p_index` (индекс опорного элемента)
    return p_index


# Раздел # с использованием схемы разделов Lomuto
def partition_random(a: list[TV], start: int, end: int):
    # Выберите случайный элемент в качестве опорного элемента из списка.
    rand_pivot_idx = random.randrange(start, end)
    pivot = a[rand_pivot_idx]

    # Элементы #, меньшие, чем точка поворота, будут перемещены влево от `p_index`
    # Элементы # больше, чем точка поворота, будут перемещены вправо от `p_index`
    # равные элементы могут идти в любом направлении
    p_index = start

    # каждый раз, когда мы находим элемент, меньший или равный опорному,
    # `p_index` увеличивается, и этот элемент будет помещен
    # перед разворотом.
    for i in range(start, end):
        if a[i] <= pivot:
            swap(a, i, p_index)
            p_index = p_index + 1

    # поменять `p_index` на пивот
    swap(a, end, p_index)

    # возвращает `p_index` (индекс опорного элемента)
    return p_index


# Процедура быстрой сортировки
def quick_sort(a: list[TV], start, end):

    # базовое состояние
    if start >= end:
        return

    # переставить элементы по оси
    pivot = partition(a, start, end)

    # повторяется в подсписке, содержащем меньше элементов, чем основной
    quick_sort(a, start, pivot - 1)

    # повторяется в подсписке, содержащем больше элементов, чем основной
    quick_sort(a, pivot + 1, end)


digit_lengths = [4, 4, 3, 3, 6, 4, 5, 4, 6, 6]  # длины слов «ноль», «один»,...


def card_strength(card: int) -> TV:  # ключ сравнения
    return digit_lengths[card]


# воспользуемся уже знакомой сортировкой вставками
def insertion_sort_by_key(array: list[TV], key: Callable[[int], TV]):
    for i in range(1, len(array)):
        item_to_insert = array[i]
        j = i
        # заменим сравнение item_to_insert < array[j-1] на сравнение ключей
        while j > 0 and key(item_to_insert) < key(array[j - 1]):
            array[j] = array[j - 1]
            j -= 1
        array[j] = item_to_insert


def is_first_card_weaker(card_1: int, card_2: int) -> bool:  # функция-компаратор
    return digit_lengths[card_1] < digit_lengths[card_2]


# воспользуемся уже знакомой сортировкой вставками
def insertion_sort_by_comparator(array: list[TV], less: Callable[[TV, TV], bool]):
    for i in range(1, len(array)):
        item_to_insert = array[i]
        j = i
        # заменим сравнение item_to_insert < array[j-1] на компаратор less
        while j > 0 and less(item_to_insert, array[j - 1]):
            array[j] = array[j - 1]
            j -= 1
        array[j] = item_to_insert


def main():
    cards = [3, 7, 9, 2, 3]
    # insertion_sort_by_key(cards, card_strength)
    print(sorted(cards, key=lambda card: [-digit_lengths[card], card]))
    pass


if __name__ == "__main__":
    main()
    pass
