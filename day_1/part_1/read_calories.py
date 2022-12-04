def get_max(first, second):
    if first is None:
        return second
    if second is None:
        return first
    return max(first, second)


with open("../input.txt") as file:
    max_calories = None
    calories = None

    for line in file:
        line = line.rstrip()
        print(line)
        if len(line) == 0:
            max_calories = get_max(calories, max_calories)
            calories = None
        else:
            if calories is None:
                calories = int(line)
            else:
                calories += int(line)

    max_calories = get_max(calories, max_calories)
    print("\nMax:", max_calories)
