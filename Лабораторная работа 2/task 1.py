def min_search(arr: List[int]) -> int:
    """
    Функция для поиска минимума в массиве
    :param arr: Массив целых чисел
    :return: Индекс первого вхождения элемента в массиве
    """
    min_idx = 0
    for i in range(1, len(arr)):
        if arr[i] < arr[min_idx]:
            min_idx = i
    return min_idx
