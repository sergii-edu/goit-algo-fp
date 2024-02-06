import uuid
import networkx as nx
import matplotlib.pyplot as plt
import heapq
from collections import deque

from helpers.shuffle_array import shuffle_array
from helpers.colors import get_gradient_color


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())


def count_nodes(node):
    if node is None:
        return 0
    return 1 + count_nodes(node.left) + count_nodes(node.right)


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2**layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2**layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def draw_tree(tree_root, title=""):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]["color"] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]["label"] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(
        tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors
    )
    plt.figtext(0.05, 0.9, title, ha="left", fontsize=14, color="black")
    plt.show()


def build_binary_tree(heap, i=0):
    if i >= len(heap):
        return None
    node = Node(heap[i])
    left_index = 2 * i + 1
    right_index = 2 * i + 2
    node.left = build_binary_tree(heap, left_index)
    node.right = build_binary_tree(heap, right_index)
    return node


def color_tree(func, root_node):
    index = 0
    nodes_count = count_nodes(root_node)

    def set_node_color(node):
        nonlocal index
        index += 1
        return setattr(
            node,
            "color",
            get_gradient_color(index / nodes_count),
        )

    func(
        root_node,
        set_node_color,
    )


def dfs(node, callback):
    if node is not None:
        callback(node)
        dfs(node.left, callback)
        dfs(node.right, callback)


def bfs(root, callback):
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node is not None:
            callback(node)
            queue.append(node.left)
            queue.append(node.right)


def main():
    heap = shuffle_array([i for i in range(1, 13)])
    heapq.heapify(heap)
    tree_root = build_binary_tree(heap)

    # Розфарбування дерева за допомогою алгоритму обходу в глибину
    color_tree(dfs, tree_root)
    draw_tree(tree_root, "Обхід в глибину")

    # Розфарбування дерева за допомогою алгоритму обходу в ширину
    color_tree(bfs, tree_root)
    draw_tree(tree_root, "Обхід в ширину")


if __name__ == "__main__":
    main()
