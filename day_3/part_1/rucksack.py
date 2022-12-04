LOWER_OFFSET = 96
UPPER_OFFSET = 64 - 26

with open("../input.txt") as file:
    total_priority = 0
    for line in file:
        line = line.rstrip()
        first = set(line[:len(line)//2])
        second = set(line[len(line)//2:])
        both = first.intersection(second)
        print(both)
        for item in both:
            if item.islower():
                priority = ord(item) - LOWER_OFFSET
            else:
                priority = ord(item) - UPPER_OFFSET
            print(priority)
            total_priority += priority

    print("\nTotal priority:", total_priority)
