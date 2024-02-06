def interpolate_color(start_color, end_color, factor):
    return start_color + factor * (end_color - start_color)


def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip("#")
    return tuple(int(hex_color[i : i + 2], 16) for i in (0, 2, 4))


def rgb_to_hex(rgb_color):
    return "#{:02x}{:02x}{:02x}".format(*rgb_color)


colors = [
    "#440154",
    "#482878",
    "#3e4989",
    "#31688e",
    "#26828e",
    "#1f9e89",
    "#35b779",
    "#6ece58",
    "#b5de2b",
    "#fde725",
]


def get_gradient_color(input_value):
    rgb_colors = [hex_to_rgb(color) for color in colors]

    if input_value <= 0:
        return colors[0]
    elif input_value >= 1:
        return colors[-1]
    else:
        position = input_value * (len(colors) - 1)
        index = int(position)
        fraction = position - index

        start_color, end_color = rgb_colors[index], rgb_colors[index + 1]
        interpolated = tuple(
            int(start_color[i] + (end_color[i] - start_color[i]) * fraction)
            for i in range(3)
        )

        return rgb_to_hex(interpolated)
