LOWER_OFFSET = 96
UPPER_OFFSET = 64 - 26

with open("../input.txt") as file:
    lines = file.read().splitlines()
    groups = list(zip(*[iter(lines)] * 3))
    total_priority = 0
    for group in groups:
        print(group)
        sets = [set(rucksack) for rucksack in group]
        badge = set.intersection(*sets)
        badge = next(iter(badge))
        print(badge)
        if badge.islower():
            priority = ord(badge) - LOWER_OFFSET
        else:
            priority = ord(badge) - UPPER_OFFSET
        print(priority)
        total_priority += priority

    print("\nTotal priority:", total_priority)
