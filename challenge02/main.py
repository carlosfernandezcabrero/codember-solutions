POSSIBLE_WORD_LENGTH = [3, 2]
ASCII_CODE_A = 97
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
            code = int(input[count : count + length])

            if code >= ASCII_CODE_A and code <= ASCII_CODE_Z:
                result += chr(code)
                count += length
                break

    return result


if __name__ == "__main__":
    solution = main()

    print(f"Result-> {solution}")
