import re
import pprint
LIMIT = 100000


def sum_dirs(dirs, initial_key, overall_sum):
    dir_sum = 0
    for key in dirs[initial_key]:
        if key.isnumeric():
            dir_sum += int(key)
        else:
            (overall_sum, subdir_sum) = sum_dirs(dirs, key, overall_sum)
            dir_sum += subdir_sum

    if dir_sum <= LIMIT:
        overall_sum += dir_sum
    return (overall_sum, dir_sum)


with open("../input.txt") as file:
    dirs = {}
    current_dir = None
    for line in file:
        if re.search(r"^\$ cd \/\n", line) is not None:
            current_dir = "/"
        elif (match := re.search(r"^\$ cd ([a-zA-Z]+)\n", line)) is not None:
            current_dir += match.group(1) + "/"
        if (match := re.search(r"^\$ cd (\.\.)\n", line)) is not None:
            current_dir = current_dir.rsplit("/", 2)[0] + "/"
        elif re.search(r"^\$ ls\n", line) is not None:
            continue
        elif (match := re.search(r"^dir (.+)\n", line)) is not None:
            dirs.setdefault(current_dir, [])
            dirs[current_dir].append(current_dir + match.group(1) + "/")
        elif (match := re.match(r"^(\d+)\s.+", line)) is not None:
            dirs.setdefault(current_dir, [])
            dirs[current_dir].append(match.group(1))

    pprint.pprint(dirs)
    (overall_sum, dir_sum) = sum_dirs(dirs, "/", 0)
    print(f"\nSum of dirs at most {LIMIT} is: {overall_sum}")
