import re
import pprint
LIMIT = 100000


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
    overall_sum = sum(list(filter(lambda x: x <= LIMIT, dirs.values())))
    print(f"\nSum of dirs at most {LIMIT} is: {overall_sum}")
