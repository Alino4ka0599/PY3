from typing import Union
import networkx as nx


def build_stairway_graph(stairway: tuple) -> nx.DiGraph:
    """
    Функция для создания графа лестницы
    :param stairway: Кортеж, содержащий стоимости каждой ступени
    :return: Взвешенный направленный граф NetworkX
    """
    n = len(stairway)
    graph = nx.DiGraph()

    for i in range(n):
        graph.add_node(i)

    for i in range(n-1):
        for j in range(i+1, n):
            if j-i <= 2:
                graph.add_edge(i, j, weight=stairway[j])

    return graph


def stairway_path(graph: nx.DiGraph) -> Union[float, int]:
    """
    Рассчитывает минимальную стоимость подъема на верхнюю ступень, если мальчик умеет наступать на следующую
    ступень и перешагивать через одну.
    :param graph: Взвешенный направленный граф NetworkX, по которому надо рассчитать стоимости кратчайших путей
    :return: Минимальная стоимость подъема на верхнюю ступень
    """
    return nx.shortest_path_length(graph, source=0, target=graph.number_of_nodes()-1, weight='weight')


if __name__ == '__main__':
    stairway = (5, 11, 43, 2, 23, 43, 22, 12, 6, 8)
    stairway_graph = build_stairway_graph(stairway)
    print(stairway_path(stairway_graph))  # 72
