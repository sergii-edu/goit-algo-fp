import heapq
import networkx as nx
import matplotlib.pyplot as plt
from tabulate import tabulate

nodes = [
    "Київ",
    "Житомир",
    "Старокостянтинів",
    "Хмельницький",
    "Тернопіль",
    "Львів",
    "Луцьк",
    "Дубно",
    "Рівне",
    "Броди",
]
G_description = [
    ("Київ", "Житомир", 132),
    ("Житомир", "Старокостянтинів", 150),
    ("Старокостянтинів", "Хмельницький", 50),
    ("Тернопіль", "Хмельницький", 110),
    ("Тернопіль", "Дубно", 109),
    ("Тернопіль", "Броди", 105),
    ("Львів", "Броди", 103),
    ("Львів", "Тернопіль", 127),
    ("Львів", "Луцьк", 150),
    ("Дубно", "Луцьк", 56),
    ("Дубно", "Рівне", 45),
    ("Дубно", "Броди", 63),
    ("Старокостянтинів", "Рівне", 148),
    ("Житомир", "Рівне", 190),
]


def dijkstra(graph, start):
    distances = {node: float("infinity") for node in graph}
    distances[start] = 0

    heap = [(0, start)]

    results = {node: {"distance": float("infinity"), "path": []} for node in graph}
    results[start]["distance"] = 0

    while heap:
        current_distance, current_node = heapq.heappop(heap)

        if current_distance > distances[current_node]:
            continue

        for neighbor, details in graph[current_node].items():
            distance = current_distance + details["weight"]

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(heap, (distance, neighbor))
                results[neighbor]["distance"] = distance
                results[neighbor]["path"] = results[current_node]["path"] + [
                    current_node
                ]

    for node in results:
        if results[node]["path"]:
            results[node]["path"].append(node)

    return results


def draw_graph(G):
    pos = nx.spring_layout(G)

    plt.figure(figsize=(12, 8))
    nx.draw(
        G,
        pos,
        with_labels=True,
        node_size=700,
        node_color="skyblue",
        font_size=10,
        font_weight="bold",
    )
    nx.draw_networkx_edge_labels(
        G, pos, edge_labels=nx.get_edge_attributes(G, "weight")
    )

    nx.draw_networkx_nodes(
        G, pos, nodelist=["Київ"], node_size=700, node_color="lightgreen"
    )

    plt.show()


def main():
    G = nx.Graph()
    G.add_nodes_from(nodes)
    G.add_weighted_edges_from(G_description)

    dijkstra_results = dijkstra(G, "Київ")

    table_data = []
    for node, details in dijkstra_results.items():
        if node != "Київ":
            route = " -> ".join(details["path"])
            length = details["distance"]
            table_data.append([node, route, length])

    print(
        tabulate(
            table_data,
            headers=["Місто", "Маршрут", "Відстань"],
            tablefmt="grid",
        )
    )

    draw_graph(G)


if __name__ == "__main__":
    main()
