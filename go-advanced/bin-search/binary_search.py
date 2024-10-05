#!/usr/bin/env python3

from typing import Callable

MIN_INT = -9223372036854775808


def binary_search(arr, x, left: int, right: int) -> int:
    if right <= left:  # промежуток пуст
        return MIN_INT
    # промежуток не пуст
    mid = (left + right) // 2
    if arr[mid] == x:  # центральный элемент — искомый
        return mid
    elif x < arr[mid]:  # искомый элемент меньше центрального значит следует искать в левой половине
        return binary_search(arr, x, left, mid)
    else:  # иначе следует искать в правой половине
        return binary_search(arr, x, mid + 1, right)


def left_binary_search(left: int, right: int, check: Callable[[int], bool]) -> int:
    if left > right:
        return MIN_INT
    while left < right:
        middle = (left + right) // 2
        if check(middle):
            right = middle
        else:
            left = middle + 1
    if check(left):
        return left
    return MIN_INT


def right_binary_search(left: int, right: int, check: Callable[[int], bool]) -> int:
    if left > right:
        return MIN_INT
    while left < right:
        middle = (left + right + 1) // 2
        if check(middle):
            left = middle
        else:
            right = middle - 1
    if check(left):
        return left
    return MIN_INT

# изначально мы запускаем двоичный поиск на всей длине массива
# index = binary_search(arr, x, left = 0, right = len(arr))
