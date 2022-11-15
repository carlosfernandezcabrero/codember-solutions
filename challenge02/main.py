with open("./input.txt", "r") as f:
    input = f.read()
    result = ""
    count = 0

    while count < len(input):
        chars_read = 0
        letter_to_add = ""

        next_char = input[count]

        if next_char == " ":
            letter_to_add = " "
            chars_read = 1
        else:
            letters = input[count : count + 3]
            code = int(letters)

            if code > 99 and code < 123:
                letter_to_add = chr(code)
                chars_read = 3

            if chars_read == 0:
                letters = letters[:2]
                code = int(letters)

                if code > 96 and code < 100:
                    letter_to_add = chr(code)
                    chars_read = 2

        result += letter_to_add
        count += chars_read

    print(f"Result-> {result}")
