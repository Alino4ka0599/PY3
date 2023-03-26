def counting_sorting(list_number):
    """
    Реализация сортировки подсчетом

    :param list_number: Массив, который нужно отсортировать
    :return: Отсортированный в порядке возрастания массив
    """

    scope = max(list_number) + 1
    c = [0] * scope
    for x in list_number:
        c[x] += 1
    list_number.clear()
    for i in range(scope):
        list_number += [i] * c[i]
    return list_number


if __name__ == '__main__':
    l_num = [1, 2, 3, 6, 6, 6, 6, 4, 200, 4, 4, 5, 1]
    result_sort = counting_sorting(l_num)

    print('Результат сортировки: ', result_sort)
