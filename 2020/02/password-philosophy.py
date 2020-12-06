
def password_philosophy():
    with open('input') as f:
        passwords = f.read().splitlines()

    part_one = None
    part_two = None

    valid_passwords = solve_part_one(passwords)

    print(f'Part 1: {valid_passwords} valid passwords')


def solve_part_one(passwords):
    valid_passwords = []
    for password in passwords:
        policy, password = password.split(': ')[0], password.split(': ')[1]
        required_frequency, letter = policy.split(' ')[0], policy[-1]
        range_min, range_max = int(required_frequency.split('-')[0]), int(required_frequency.split('-')[1])

        actual_frequency = 0
        for char in password:
            if char is letter:
                actual_frequency += 1

        if actual_frequency in range(range_min, range_max + 1):
            valid_passwords.append(password)

    return len(valid_passwords)


def solve_part_two():
    pass


if __name__ == "__main__":
    password_philosophy()
