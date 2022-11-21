POSSIBLE_WORD_LENGTH = [3, 2]
ASCII_CODE_Z = 122

f = open("./input.txt", "r")
input = f.read()
f.close()


def main():
    result = ""
    count = 0

    while count < len(input):
        next_char = input[count]

        if next_char == " ":
            result += " "
            count += 1
            continue

        for length in POSSIBLE_WORD_LENGTH:
            letter = input[count : count + length]

            if " " in letter:
                continue

            code = int(letter)
            lower_limit = 10 ** (length - 1)
            upper_limit = ASCII_CODE_Z if length == 3 else 10**length

            if code >= lower_limit and code <= upper_limit:
                result += chr(code)
                count += length
                break

    return result


if __name__ == "__main__":
    solution = main()

    print(f"Result-> {solution}")
