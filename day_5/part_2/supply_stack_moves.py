# Initial stacks:
#
# [N]     [C]                 [Q]
# [W]     [J] [L]             [J] [V]
# [F]     [N] [D]     [L]     [S] [W]
# [R] [S] [F] [G]     [R]     [V] [Z]
# [Z] [G] [Q] [C]     [W] [C] [F] [G]
# [S] [Q] [V] [P] [S] [F] [D] [R] [S]
# [M] [P] [R] [Z] [P] [D] [N] [N] [M]
# [D] [W] [W] [F] [T] [H] [Z] [W] [R]
#  1   2   3   4   5   6   7   8   9

stacks = []
stacks.append(list("DMSZRFWN"))
stacks.append(list("WPQGS"))
stacks.append(list("WRVQFNJC"))
stacks.append(list("FZPCGDL"))
stacks.append(list("TPS"))
stacks.append(list("HDFWRL"))
stacks.append(list("ZNDC"))
stacks.append(list("WNRFVSJQ"))
stacks.append(list("RMSGZWV"))

with open("../input_moves.txt") as file:
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
