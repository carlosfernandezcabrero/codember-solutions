import re

keys_to_search = ["usr", "eme", "psw", "age", "loc", "fll"]

with open("./input.txt", encoding="utf-8") as f:
    data = f.read()
    users = data.split("\n\n")
    valid_users = 0
    last_valid_user = None

    for user in users:
        valid = True

        for key in keys_to_search:
            if key not in user:
                valid = False
                break

        if valid:
            last_valid_user = re.search(r"usr:([\w@\d]+)\s.*", user).group(1)
            valid_users += 1

    print(f"{valid_users}{last_valid_user}")
