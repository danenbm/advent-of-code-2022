def overlaps(first, second):
    if first[0] >= second[0]:
        if first[0] <= second[1]:
            return True
    return False


with open("../input.txt") as file:
    total = 0

    for line in file:
        line = line.rstrip()
        sections = line.split(',')
        sections = [list(map(int, section.split('-'))) for section in sections]
        print(sections)
        if overlaps(sections[0], sections[1]):
            total += 1
        elif overlaps(sections[1], sections[0]):
            total += 1

    print("\nSum of overlaps:", total)
