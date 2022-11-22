from input import input


def main(colors: list[str]) -> str:
    colors_object: dict[str, list[int]] = {}

    for idx, color in enumerate(colors):
        if color in colors_object:
            colors_object[color].append(idx)
        else:
            colors_object[color] = [idx]

    colors_object_keys: list[str] = list(colors_object.keys())
    if len(colors) == len(colors_object_keys):
        return f"{colors} -> 2, {colors_object_keys[-1]}"

    if len(colors_object_keys) == 2:
        return f"{colors} -> {len(colors)}, {colors[-1]}"

    if len(colors_object_keys) == 1:
        return f"{colors} -> 1, {colors[-1]}"

    zebras: list[list[str]] = []
    actual_zebra: list[str] = []

    for idx, color in enumerate(colors):
        if len(actual_zebra) == 0:
            actual_zebra.append(color)
            continue

        if actual_zebra[-1] == color:
            zebras.append(actual_zebra)
            actual_zebra = [color]
        elif len(actual_zebra) >= 2 and color not in actual_zebra:
            add_last_color: bool = False
            last_color = ""

            if idx < len(colors) - 1 and actual_zebra[-1] == colors[idx + 1]:
                add_last_color = True
                last_color = actual_zebra[-1]

            zebras.append(actual_zebra)
            actual_zebra = [color]

            if add_last_color:
                actual_zebra.insert(0, last_color)
        else:
            actual_zebra.append(color)

        if len(colors) - 1 == idx:
            zebras.append(actual_zebra)

    zebras.sort(key=len, reverse=True)

    return f"{colors} -> {len(zebras[0])}, {zebras[0][-1]}"


if __name__ == "__main__":
    solution = main(input)
    print(solution)
