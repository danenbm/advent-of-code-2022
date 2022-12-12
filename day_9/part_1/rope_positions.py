X = 0
Y = 1
head_pos = [0, 0]
tail_pos = [0, 0]
visited_by_tail = set(tuple(tail_pos))

with open("../input.txt") as file:
    for line in file:
        (dir, amount) = line.split()
        amount = int(amount)

        for i in range(amount):
            # Move head.
            if dir == 'R':
                head_pos[X] += 1
            elif dir == 'L':
                head_pos[X] -= 1
            elif dir == 'U':
                head_pos[Y] += 1
            elif dir == 'D':
                head_pos[Y] -= 1

            x_diff = head_pos[X] - tail_pos[X]
            if abs(x_diff) >= 2:
                tail_pos[X] += x_diff // 2

                y_diff_d = head_pos[Y] - tail_pos[Y]
                if abs(y_diff_d) > 0:
                    tail_pos[Y] += y_diff_d

                visited_by_tail.add(tuple(tail_pos))

            y_diff = head_pos[Y] - tail_pos[Y]
            if abs(y_diff) >= 2:
                tail_pos[Y] += y_diff // 2

                x_diff_d = head_pos[X] - tail_pos[X]
                if abs(x_diff_d) > 0:
                    tail_pos[X] += x_diff_d

                visited_by_tail.add(tuple(tail_pos))

    print(f"\nTotal positions visited by tail: {len(visited_by_tail)}")
