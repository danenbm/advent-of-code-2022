import re
import pprint
TOTAL_FS_SIZE = 70000000
MIN_NEEDED = 30000000


def sum_dirs(dirs, initial_key, current_choice=None, additional_needed=None):
    dir_sum = 0
    for key in dirs[initial_key]:
        if key.isnumeric():
            dir_sum += int(key)
        else:
            (current_choice, subdir_sum) = sum_dirs(dirs,
                                                    key,
                                                    current_choice,
                                                    additional_needed)
            dir_sum += subdir_sum

    if additional_needed is not None and dir_sum >= additional_needed:
        if current_choice is None or dir_sum < current_choice:
            current_choice = dir_sum
    return (current_choice, dir_sum)


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
    (_choice, dir_sum) = sum_dirs(dirs, "/")
    print(f"\nSize of '/' is: {dir_sum} ")
    unused_space = 70000000 - dir_sum
    print(f"Unused space is: {unused_space}")
    additional_needed = MIN_NEEDED - unused_space
    print(f"Additional needed space is: {additional_needed}")
    (choice, dir_sum) = sum_dirs(dirs, "/", None, additional_needed)
    print(f"Smallest dir greater than additional needed is: {choice} ")
