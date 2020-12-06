
def toboggan_trajectory():
    with open('input') as f:
        map_section = f.read().splitlines()

    expanded_map = create_map(map_section)

    trees_encountered_part_one = solve_part_one(expanded_map)

    print(f'Part 1: {trees_encountered_part_one} trees')
    # print(f'Part 2: {len(valid_passwords_part_two)} trees')


def create_map(map_section):
    rows = len(map_section)
    cols = len(map_section[0])
    cols_needed = (rows - 1) * 3
    multiplier = cols_needed / cols
    
    expanded_map = []
    for row in map_section:
        row = row * (int(multiplier) + 1)
        expanded_map.append(row)

    return expanded_map


def solve_part_one(expanded_map):
    position = 0
    trees_encountered = 0

    for row in expanded_map:
        if row[position] == '#':
            trees_encountered += 1
        position = position + 3

    return trees_encountered


def solve_part_two():
    pass


if __name__ == "__main__":
    toboggan_trajectory()
