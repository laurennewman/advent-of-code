
def toboggan_trajectory():
    with open('input') as f:
        map_section = f.read().splitlines()

    slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
    expanded_map = create_map(map_section, max([moves[0] for moves in slopes]))

    for slope in slopes:
        encounter_trees(expanded_map, slope)

    print(f'Part 1: {slopes[1][2]} trees')

    product_of_trees_encountered = multiply_trees(slopes)
    print(f'Part 2: {product_of_trees_encountered} trees')


def create_map(map_section, moves_to_the_right):
    rows = len(map_section)
    cols = len(map_section[0])
    cols_needed = (rows - 1) * moves_to_the_right
    multiplier = cols_needed / cols

    expanded_map = []
    for row in map_section:
        row = row * (int(multiplier) + 1)
        expanded_map.append(row)

    return expanded_map


def encounter_trees(expanded_map, slope):
    x_position = 0
    y_position = 0
    move_right = slope[0]
    move_down = slope[1]

    trees_encountered = 0
    while len(expanded_map) > y_position:
        if expanded_map[y_position][x_position] == '#':
            trees_encountered += 1
        x_position = x_position + move_right
        y_position = y_position + move_down

    slope.append(trees_encountered)


def multiply_trees(slopes):
    result = 1
    for slope in slopes:
        result = result * slope[2]
    return result


if __name__ == "__main__":
    toboggan_trajectory()
