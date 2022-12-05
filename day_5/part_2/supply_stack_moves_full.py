import re

stacks = None
with open("../input_raw.txt") as file:
    for line in file:
        if line == "\n":
            print("")
            break
        crates_row = re.findall(".(.).\s", line)
        print(crates_row)

        if stacks is None:
            stacks = [[] for i in range(len(crates_row))]
        for i in range(len(crates_row)):
            if crates_row[i] != ' ':
                stacks[i].insert(0, crates_row[i])

    for line in file:
        moves = line.split()
        print(moves)
        quantity = int(moves[1])
        source = int(moves[3]) - 1
        dest = int(moves[5]) - 1
        crates = stacks[source][-quantity:]
        del stacks[source][-quantity:]
        stacks[dest].extend(crates)

    message = []
    for stack in stacks:
        crate = stack.pop()
        message.append(crate)

    print("\nFinal crate message:", ''.join(message))
