def get_top_n(candidate, top_n_list, n):
    if candidate is None:
        return top_n_list
    if len(top_n_list) < n:
        top_n_list.append(candidate)
    else:
        min_of_top_n = min(top_n_list)
        if candidate > min_of_top_n:
            index = top_n_list.index(min_of_top_n)
            top_n_list[index] = candidate
    return top_n_list


with open("../input.txt") as file:
    top_three = []
    calories = None

    for line in file:
        line = line.rstrip()
        print(line)
        if len(line) == 0:
            top_three = get_top_n(calories, top_three, 3)
            calories = None
        else:
            if calories is None:
                calories = int(line)
            else:
                calories += int(line)

    top_three = get_top_n(calories, top_three, 3)
    print("\nTop three:", top_three)
    print("Sum of top three:", sum(top_three))
