import string
from pickle import LIST
from typing import Dict, List, Tuple


def build_filesystem() -> Dict[str, List[Tuple[int, str]]]:
    lines: List[str] = [l.strip() for l in open("data.txt", "r").readlines()]
    curr_path = ""
    path_map: Dict[str, List[Tuple[int, str]]] = {}
    indi = 0
    while indi < len(lines):
        line = lines[indi]
        if line.startswith("$"):
            line_s = line.replace("$ ", "").split(" ")
            if line_s[0] == "cd" and line_s[1] == "/":
                curr_path = ""
                indi += 1
            elif line_s[0] == "cd" and line_s[1] == "..":
                curr_path_l = curr_path.split("/")
                curr_path = "/".join(curr_path_l[0:len(curr_path_l) - 1])
                indi += 1
            elif line_s[0] == "cd":
                curr_path = curr_path + "/" + line_s[1]
                indi += 1
            else:
                file_list: List[Tuple[int, str]] = []
                while indi <= len(lines):
                    indi += 1
                    if indi >= len(lines):
                        break
                    line = lines[indi]
                    if line.startswith("$"):
                        break
                    else:
                        l = lines[indi].split(" ")
                        if l[0][0] in string.ascii_lowercase:
                            file_list.append((0, curr_path + "/" + l[1]))
                        else:
                            file_list.append((int(l[0]), l[1]))
                # print(file_list)
                try:
                    path_map[curr_path].extend(file_list)
                except KeyError:
                    path_map[curr_path] = file_list
    return path_map


def part_1() -> List[int]:
    path_map = build_filesystem()
    dir_l = []
    all_dir = []

    def compute_filesize(ley: str) -> int:
        dir_size = 0
        if path_map.get(ley) == None:
            return 0
        itms = path_map[ley]
        for itm in itms:
            if itm[0] == 0:
                dir_size += compute_filesize(itm[1])
            else:
                dir_size += itm[0]
        if dir_size <= 100000:
            dir_l.append(dir_size)
        all_dir.append(dir_size)
        return dir_size

    compute_filesize("")
    print("Part 1:")
    print(sum(dir_l))
    return all_dir


def part_2(all_dir: List[int]):
    tot_space = max(all_dir)
    max_s = 70000000
    gl_ss = 30000000
    unused = max_s - tot_space
    all_d = [dir_s for dir_s in all_dir if gl_ss <= (dir_s + unused)]
    print("Part 2:")
    print(min(all_d))


part_2(part_1())
