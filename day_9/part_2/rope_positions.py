X = 0
Y = 1
TOTAL_KNOTS = 10
knot_pos = [[0, 0] for i in range(TOTAL_KNOTS)]
visited_by_tail = set(tuple(knot_pos[9]))

with open("../input.txt") as file:
    for line in file:
        (dir, amount) = line.split()
        amount = int(amount)

        for i in range(amount):
            # Move head.
            if dir == 'R':
                knot_pos[0][X] += 1
            elif dir == 'L':
                knot_pos[0][X] -= 1
            elif dir == 'U':
                knot_pos[0][Y] += 1
            elif dir == 'D':
                knot_pos[0][Y] -= 1

            for j in range(TOTAL_KNOTS - 1):
                head_pos = knot_pos[j]
                tail_pos = knot_pos[j + 1]

                x_diff = head_pos[X] - tail_pos[X]
                y_diff = head_pos[Y] - tail_pos[Y]
                if abs(x_diff) == 2 and abs(y_diff) == 2:
                    tail_pos[X] += x_diff // 2
                    tail_pos[Y] += y_diff // 2

                    if (j + 1) == (TOTAL_KNOTS - 1):
                        visited_by_tail.add(tuple(tail_pos))

                else:
                    if abs(x_diff) >= 2:
                        tail_pos[X] += x_diff // 2

                        y_diff_d = head_pos[Y] - tail_pos[Y]
                        if abs(y_diff_d) > 0:
                            tail_pos[Y] += y_diff_d

                        if (j + 1) == (TOTAL_KNOTS - 1):
                            # print(tuple(tail_pos))
                            visited_by_tail.add(tuple(tail_pos))

                    if abs(y_diff) >= 2:
                        tail_pos[Y] += y_diff // 2

                        x_diff_d = head_pos[X] - tail_pos[X]
                        if abs(x_diff_d) > 0:
                            tail_pos[X] += x_diff_d

                        if (j + 1) == (TOTAL_KNOTS - 1):
                            # print(tuple(tail_pos))
                            visited_by_tail.add(tuple(tail_pos))

    print(visited_by_tail)
    print(f"\nTotal positions visited by last knot: {len(visited_by_tail)}")
