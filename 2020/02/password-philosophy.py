
def password_philosophy():
    with open('input') as f:
        passwords = f.read().splitlines()

    valid_passwords_part_one = []
    valid_passwords_part_two = []

    split_passwords = split(passwords)

    for split_password in split_passwords:
        rule_one = split_password[0]
        rule_two = split_password[1]
        letter = split_password[2]
        password = split_password[3]

        solve_part_one(rule_one, rule_two, letter, password, valid_passwords_part_one)
        solve_part_two(rule_one, rule_two, letter, password, valid_passwords_part_two)

    print(f'Part 1: {len(valid_passwords_part_one)} valid passwords')
    print(f'Part 2: {len(valid_passwords_part_two)} valid passwords')


def split(passwords):
    split_passwords = []
    for password in passwords:
        policy, password = password.split(': ')[0], password.split(': ')[1]
        required_frequency, letter = policy.split(' ')[0], policy[-1]
        rule_one, rule_two = int(required_frequency.split('-')[0]), int(required_frequency.split('-')[1])
        split_passwords.append([rule_one, rule_two, letter, password])

    return split_passwords


def solve_part_one(rule_one, rule_two, letter, password, valid_passwords_part_one):
    actual_frequency = 0
    for char in password:
        if char is letter:
            actual_frequency += 1

    if actual_frequency in range(rule_one, rule_two + 1):
        valid_passwords_part_one.append(password)


def solve_part_two(rule_one, rule_two, letter, password, valid_passwords_part_two):
    rule_one = rule_one - 1
    rule_two = rule_two - 1

    if password[rule_one] is letter and password[rule_two] is not letter:
        valid_passwords_part_two.append(password)

    if password[rule_one] is not letter and password[rule_two] is letter:
        valid_passwords_part_two.append(password)


if __name__ == "__main__":
    password_philosophy()
