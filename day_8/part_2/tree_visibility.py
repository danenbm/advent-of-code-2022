with open("../input.txt") as file:
    trees = [line.rstrip() for line in file]
    width = len(trees[0])
    height = len(trees)
    print(trees)

    max_score = None
    for row in range(0, height):
        for column in range(0, width):
            tree = trees[row][column]

            # Check view to left.
            left_score = 0
            for check_column in range(column - 1, -1, -1):
                left_score += 1
                if trees[row][check_column] >= tree:
                    break

            # Check view to right.
            right_score = 0
            for check_column in range(column + 1, width):
                right_score += 1
                if trees[row][check_column] >= tree:
                    break

            # Check view above.
            top_score = 0
            for check_row in range(row - 1, -1, -1):
                top_score += 1
                if trees[check_row][column] >= tree:
                    break

            # Check view below.
            bottom_score = 0
            for check_row in range(row + 1, height):
                bottom_score += 1
                if trees[check_row][column] >= tree:
                    break

            total_score = left_score * right_score * top_score * bottom_score
            if max_score is None:
                max_score = total_score
            elif total_score > max_score:
                max_score = total_score

    print(f"\nHighest score: {max_score}")
