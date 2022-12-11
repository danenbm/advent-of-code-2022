with open("../input.txt") as file:
    trees = [line.rstrip() for line in file]
    width = len(trees[0])
    height = len(trees)
    print(trees)

    # All outside trees are visible.
    num_visible = 2 * width + 2 * (height - 2)

    # Make a list of max values of all trees to the right.
    right_maxes = [['']]
    for row in range(1, height - 1):
        right_maxes.append([trees[row][width - 1]])
        for column in range(width - 2, -1, -1):
            if trees[row][column] > right_maxes[row][0]:
                right_maxes[row].insert(0, trees[row][column])
            else:
                right_maxes[row].insert(0, right_maxes[row][0])

    # Make a list of max values of all trees above.
    top_maxes = [['']]
    for column in range(1, width - 1):
        top_maxes.append([trees[0][column]])
        for row in range(1, height):
            if trees[row][column] > top_maxes[column][-1]:
                top_maxes[column].append(trees[row][column])
            else:
                top_maxes[column].append(top_maxes[column][-1])

    # Make a list of max values of all trees below.
    bottom_maxes = [['']]
    for column in range(1, width - 1):
        bottom_maxes.append([trees[height - 1][column]])
        for row in range(height - 2, -1, -1):
            if trees[row][column] > bottom_maxes[column][0]:
                bottom_maxes[column].insert(0, trees[row][column])
            else:
                bottom_maxes[column].insert(0, bottom_maxes[column][0])

    # We don't need a list for max values to the left.
    # That will be determined with the final traversal
    # where we are checking left, right, above, and below
    # and choosing visibility if any of those are true.
    for row in range(1, height - 1):
        left_max = trees[row][0]
        for column in range(1, width - 1):
            tree = trees[row][column]
            if tree > left_max:
                num_visible += 1
                left_max = tree
            elif tree > right_maxes[row][column + 1]:
                num_visible += 1
            elif tree > top_maxes[column][row - 1]:
                num_visible += 1
            elif tree > bottom_maxes[column][row + 1]:
                num_visible += 1

    print(f"\nTotal num visible: {num_visible}")
