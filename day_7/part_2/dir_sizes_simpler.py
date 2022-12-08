import re
import pprint
TOTAL_FS_SIZE = 70000000
MIN_NEEDED = 30000000


with open("../input.txt") as file:
    dirs = {}
    for line in file:
        if re.search(r"^\$ cd \/\n", line) is not None:
            current_dir = "/"
        elif (match := re.search(r"^\$ cd ([a-zA-Z]+)\n", line)) is not None:
            current_dir += match.group(1) + "/"
        if (match := re.search(r"^\$ cd (\.\.)\n", line)) is not None:
            current_dir = current_dir.rsplit("/", 2)[0] + "/"
        elif (match := re.match(r"^(\d+)\s.+", line)) is not None:
            dirs.setdefault(current_dir, 0)
            val = int(match.group(1))
            dirs[current_dir] += val

            dir = current_dir
            while (dir != "/"):
                dir = dir.rsplit("/", 2)[0] + "/"
                dirs.setdefault(dir, 0)
                dirs[dir] += val

    pprint.pprint(dirs)
    root_sum = dirs["/"]
    print(f"\nSize of '/' is: {root_sum} ")
    unused_space = 70000000 - root_sum
    print(f"Unused space is: {unused_space}")
    additional_needed = MIN_NEEDED - unused_space
    print(f"Additional needed space is: {additional_needed}")
    choice = min(list(filter(lambda x: x >= additional_needed, dirs.values())))
    print(f"Smallest dir greater than additional needed is: {choice} ")
