from math import inf
from collections import defaultdict

graph = {
    1: {2: 4, 3: 3},
    2: {1: 4, 4: 6, 6: 2},
    3: {1: 3, 5: 2, 6: 8},
    4: {2: 6, 6: 1, 7: 3},
    5: {3: 2, 6: 4, 7: 2},
    6: {2: 2, 3: 8, 4: 1, 5: 4},
    7: {4: 3, 5: 2}
}

path_len = defaultdict(lambda: inf)
visited = set()
node = 1
value = 0
final_node = 7

path_len[node] = value
while node != final_node and visited != set(graph.keys()):
    for next_node in (graph[node].keys() - visited):
        new_value = value + graph[node][next_node]
        if new_value < path_len[next_node]:
            path_len[next_node] = new_value
    visited.add(node)
    path_len[node] = inf
    node, value = max((node, value) for node, value in path_len.items() if node not in visited)

print(path_len[final_node])
"""
1. path_len = defaultdict(lambda: inf): 
   В этой строке создается словарь path_len с использованием defaultdict. 
   defaultdict - это подкласс стандартного словаря в Python, который позволяет 
   устанавливать значение по умолчанию для ключей, которые еще не существуют в словаре. 
   В данном случае, когда вы обращаетесь к path_len с ключом, которого нет в словаре, 
   автоматически создается новая запись с значением inf (бесконечность). 
   Это полезно в алгоритме поиска кратчайшего пути, где inf используется для 
   представления бесконечно большого расстояния.

2. path_len.pop(node): 
   В этой строке выполняется удаление элемента с ключом node из словаря path_len. 
   Вероятно, эта строка используется для того, чтобы пометить узел как посещенный. 
   Однако, есть потенциальная проблема в том, что это может вызвать KeyError, если 
   node отсутствует в словаре. Возможно, было бы лучше использовать path_len[node] = inf 
   для установки значения в inf, чтобы пометить узел как посещенный.

3. key=lambda x: x[1]: 
   Этот аргумент используется в различных функциях, таких как max или sorted. 
   Эта конструкция позволяет указать функцию для извлечения ключа, по которому будет 
   производится сортировка или выбор максимального элемента. 
   В данном случае, lambda x: x[1] означает, что будет использоваться второй элемент 
   кортежа x в качестве ключа для сравнения. 
   Например, если x - это пара (a, b), то сравниваться будут значения b. 
   Это полезно, когда вы хотите сортировать или выбирать элементы по какому-то конкретному критерию.
"""
"""
Отладьте представленную ниже программу, в которой реализован алгоритм Дейкстры. В результате
 работы программа должна выводить длину минимального пути от 1 до 7 вершины представленного графа:
"""