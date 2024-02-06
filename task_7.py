import numpy as np
from tabulate import tabulate


probabilities = [2.78, 5.56, 8.33, 11.11, 13.89, 16.67, 13.89, 11.11, 8.33, 5.56, 2.78]


def get_monte_carlo_probabilities(num_rolls):
    rolls = np.random.randint(1, 7, size=(num_rolls, 2))
    sums = np.sum(rolls, axis=1)

    frequencies = [np.sum(sums == i) for i in range(2, 13)]

    return np.array(frequencies) / num_rolls * 100


def print_as_table(num_rolls_list, *monte_carlo_probabilities_arrays):
    table_data = []
    for i in range(2, 13):
        row = [i, probabilities[i - 2]]
        for mc_probs in monte_carlo_probabilities_arrays:
            row.append(mc_probs[i - 2])
        table_data.append(row)

    headers = ["Сума", "Імовірність (%)"] + [
        f"Монте Карло {num_rolls} повторень (%)" for num_rolls in num_rolls_list
    ]

    table = tabulate(table_data, headers=headers, floatfmt=".2f")
    print(table)


def main():
    num_rolls_1 = 1000
    num_rolls_2 = 100000
    mc_probabilities_1 = get_monte_carlo_probabilities(num_rolls_1)
    mc_probabilities_2 = get_monte_carlo_probabilities(num_rolls_2)
    print_as_table([num_rolls_1, num_rolls_2], mc_probabilities_1, mc_probabilities_2)


if __name__ == "__main__":
    main()
