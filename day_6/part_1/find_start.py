index = 1
num_unique = 4
with open("../input.txt") as file:
    while (1):
        chars = file.read(num_unique)
        if not chars:
            break
        print(chars)
        chars = set(chars)
        print(chars)
        if len(chars) == num_unique:
            print(f"\nStart complete at loc {index + num_unique - 1}")
            break
        file.seek(index)
        index += 1
