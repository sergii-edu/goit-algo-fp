from tabulate import tabulate

items = {
    "pizza": {"cost": 50, "calories": 300},  # 300/50 = 6
    "hamburger": {"cost": 40, "calories": 250},  # 250/40 = 6.25
    "hot-dog": {"cost": 30, "calories": 200},  # 200/30 = 6.67
    "pepsi": {"cost": 10, "calories": 100},  # 100/10 = 10
    "cola": {"cost": 15, "calories": 220},  # 220/15 = 14.67
    "potato": {"cost": 25, "calories": 350},  # 350/25 = 14
}


def greedy_algorithm(items, budget):
    sorted_items = sorted(
        items.keys(),
        key=lambda x: items[x]["calories"] / items[x]["cost"],
        reverse=True,
    )

    result = {}
    total = 0
    for item in sorted_items:
        if total + items[item]["cost"] <= budget:
            result[item] = items[item]
            total += items[item]["cost"]
    return result


def dynamic_programming(items, budget):
    K = [[0 for x in range(budget + 1)] for y in range(len(items) + 1)]
    item_list = list(items.keys())
    for i in range(1, len(items) + 1):
        for w in range(1, budget + 1):
            if items[item_list[i - 1]]["cost"] <= w:
                K[i][w] = max(
                    K[i - 1][w],
                    K[i - 1][w - items[item_list[i - 1]]["cost"]]
                    + items[item_list[i - 1]]["calories"],
                )
            else:
                K[i][w] = K[i - 1][w]

    result = {}
    for i in range(len(items), 0, -1):
        if K[i][budget] != K[i - 1][budget]:
            item = item_list[i - 1]
            result[item] = items[item]
            budget -= items[item]["cost"]
    return result


def print_as_table(algorithm_results):
    table_data = []
    for item, value in algorithm_results.items():
        row = [item, value["cost"], value["calories"]]
        table_data.append(row)
    table_data.append([])
    total_cost = sum([value["cost"] for value in algorithm_results.values()])
    total_kcal = sum([value["calories"] for value in algorithm_results.values()])
    table_data.append(["TOTAL: ", total_cost, total_kcal])

    headers = ["Страва", "Вартість", "Калорії"]
    table = tabulate(
        table_data,
        headers=headers,
        floatfmt=".2f",
    )
    return table


def main():
    budget = 100

    print("Жадібний алгоритм:")
    print()
    print(print_as_table(greedy_algorithm(items, budget)))
    print()
    print()
    print("Динамічне програмування:")
    print()
    print(print_as_table(dynamic_programming(items, budget)))


if __name__ == "__main__":
    main()
