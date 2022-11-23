INITIAL_COUNT = 11098
FINAL_COUNT = 98123


def main_function():
    valid_numbers: list[str] = []

    for i in range(INITIAL_COUNT, FINAL_COUNT):
        i_str = str(i)

        if len(i_str) != 5 or i_str.count("5") < 2:
            continue

        last_digit = 0
        valid = True
        for n in i_str:
            if int(n) < last_digit:
                valid = False
                break
            last_digit = int(n)

        if valid:
            valid_numbers.append(i_str)

    return valid_numbers


if __name__ == "__main__":
    valid_numbers = main_function()

    print(f"{len(valid_numbers)}-{valid_numbers[55]}")
