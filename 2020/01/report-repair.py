
def report_repair():
    with open('input') as f:
        report = f.read().splitlines()

    report = list(map(int, report))
    part_one = None
    part_two = None

    for factor1 in report:
        factor2 = 2020 - factor1
        if not part_one:
            part_one = solve_part_one(factor1, factor2, report)
        if not part_two:
            part_two = solve_part_two(factor1, report)

    print(f'Part 1: {part_one}')
    print(f'Part 2: {part_two}')


def solve_part_one(factor1, factor2, report):
    if factor2 in report:
        return factor1 * factor2


def solve_part_two(factor1, report):
    report_copy = report.copy()
    report_copy.remove(factor1)
    for factor2 in report_copy:
        factor3 = 2020 - factor1 - factor2
        if factor3 in report_copy:
            return factor1 * factor2 * factor3


if __name__ == "__main__":
    report_repair()
