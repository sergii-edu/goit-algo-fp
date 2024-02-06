import matplotlib.pyplot as plt
import numpy as np

from helpers.colors import interpolate_color


def draw_tree(
    ax, origin, length, width, angle, depth, current_depth, start_color, end_color
):
    if depth == 0:
        return

    factor = current_depth / (initial_depth - 1) if initial_depth > 3 else 1
    color = interpolate_color(start_color, end_color, factor)

    angle_variation = (
        np.pi / 180 if current_depth == 0 else np.pi / 180 * np.random.uniform(-15, 15)
    )
    length_variation = length * np.random.uniform(-0.25, 0.25)

    end = origin + (length + length_variation) * np.array(
        [np.cos(angle + angle_variation), np.sin(angle + angle_variation)]
    )
    ax.plot([origin[0], end[0]], [origin[1], end[1]], color=color, linewidth=width)

    new_length = 1 if depth == 2 else (length + length_variation) * np.sqrt(2) / 2
    new_width = 5 if depth == 2 else width * np.sqrt(2) / 2

    draw_tree(
        ax,
        end,
        new_length,
        new_width,
        angle + np.pi / 8 + angle_variation,
        depth - 1,
        current_depth + 1,
        start_color,
        end_color,
    )
    draw_tree(
        ax,
        end,
        new_length,
        new_width,
        angle - np.pi / 8 + angle_variation,
        depth - 1,
        current_depth + 1,
        start_color,
        end_color,
    )


def pythagoras_tree(depth):
    fig, ax = plt.subplots()
    ax.set_aspect("equal")
    ax.axis("off")

    global initial_depth
    initial_depth = depth

    start_color = np.array([139 / 255, 69 / 255, 19 / 255])  # Коричневий
    end_color = np.array([34 / 255, 139 / 255, 34 / 255])  # Зелений

    origin = np.array([0, 0])
    length = 10
    width = depth / 2
    angle = np.pi / 2

    draw_tree(ax, origin, length, width, angle, depth, 0, start_color, end_color)
    plt.show()


def main():
    try:
        depth = int(input("Будь ласка, введіть рівень рекурсії для побудови дерева: "))
        pythagoras_tree(depth)
    except ValueError:
        print("Виникла помилка при введенні даних. Будь ласка, введіть ціле число.")


if __name__ == "__main__":
    main()
