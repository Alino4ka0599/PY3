def bubblesort(list_number):
    """
    Функция сортировки пузырьком

    :param list_number: Массив чисел, которые нужно отсортировать
    :return: Отсортированный список по возрастанию
    """
    for i in range(len(list_number)-1):
        stop = True
        for j in range(len(list_number)-1-i):
            if list_number[j] > list_number[j+1]:
                list_number[j], list_number[j+1] = list_number[j+1], list_number[j]
                stop = False
        if stop:
            break
    return list_number


if __name__ == '__main__':
    list_number = [14, 3, 52, 23, 53, 94, 26, 28, 56, 33, 56, 57, 86, 0, 4, 7, 12, 96, 89, 49]
    res = bubblesort(list_number)
    print('Отсортированный список чисел: ', res)

