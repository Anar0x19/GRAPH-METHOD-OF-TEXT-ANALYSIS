import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

class TextGraph:
    def __init__(self, segments):
        self.segments = segments
        self.graph = nx.DiGraph()
        self._build_graph()

    def _build_graph(self):
        """Создаем граф из сегментов текста."""
        for segment, connections in self.segments.items():
            for connection in connections:
                self.graph.add_edge(segment, connection)

    def adjacency_matrix(self):
        """Создаем и возвращаем матрицу смежности графа."""
        return nx.adjacency_matrix(self.graph).todense()

    def find_isolated_nodes(self):
        """Находим изолированные вершины."""
        isolated = list(nx.isolates(self.graph))
        return isolated

    def find_endpoints(self):
        """Находим висячие и тупиковые вершины."""
        leaves = [node for node in self.graph.nodes if self.graph.out_degree(node) == 0]
        return leaves

    def find_cycles(self):
        """Ищем циклы в графе."""
        try:
            cycles = list(nx.find_cycle(self.graph, orientation='original'))
            return cycles
        except nx.NetworkXNoCycle:
            return None

    def draw_graph(self):
        """Отображаем граф с помощью matplotlib."""
        pos = nx.spring_layout(self.graph)
        nx.draw(self.graph, pos, with_labels=True, node_color='lightblue', edge_color='gray')
        plt.show()

segments = {
    'Введение': ['Цель', 'Задачи'],
    'Цель': ['Методология', 'Результаты'],
    'Задачи': ['Методология'],
    'Методология': ['Результаты'],
    'Результаты': ['Заключение'],
    'Заключение': []
}

text_graph = TextGraph(segments)

adj_matrix = text_graph.adjacency_matrix()
print("Матрица смежности:")
print(adj_matrix)

isolated_nodes = text_graph.find_isolated_nodes()
print("Изолированные вершины:", isolated_nodes)

endpoints = text_graph.find_endpoints()
print("Тупиковые вершины:", endpoints)

cycles = text_graph.find_cycles()
print("Циклы в графе:", cycles)

text_graph.draw_graph()
