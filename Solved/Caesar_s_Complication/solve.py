#!/usr/bin/env python3
import re

# Search through ROT0 to ROT25 keywords
search_words = [
    r"tjctf\{.+\}",
    r"ukdug\{.+\}",
    r"vlevh\{.+\}",
    r"wmfwi\{.+\}",
    r"xngxj\{.+\}",
    r"yohyk\{.+\}",
    r"zpizl\{.+\}",
    r"aqjam\{.+\}",
    r"brkbn\{.+\}",
    r"cslco\{.+\}",
    r"dtmdp\{.+\}",
    r"euneq\{.+\}",
    r"fvofr\{.+\}",
    r"gwpgs\{.+\}",
    r"hxqht\{.+\}",
    r"iyriu\{.+\}",
    r"jzsjv\{.+\}",
    r"katkw\{.+\}",
    r"lbulx\{.+\}",
    r"mcvmy\{.+\}",
    r"ndwnz\{.+\}",
    r"oexoa\{.+\}",
    r"pfypb\{.+\}",
    r"qgzqc\{.+\}",
    r"rhard\{.+\}",
    r"sibse\{.+\}",
]

# Reversed direction
search_words_reversed = [
    r"\}.+\{ftcjt",
    r"\}.+\{gudku",
    r"\}.+\{hvelv",
    r"\}.+\{iwfmw",
    r"\}.+\{jxgnx",
    r"\}.+\{kyhoy",
    r"\}.+\{lzipz",
    r"\}.+\{majqa",
    r"\}.+\{nbkrb",
    r"\}.+\{oclsc",
    r"\}.+\{pdmtd",
    r"\}.+\{qenue",
    r"\}.+\{rfovf",
    r"\}.+\{sgpwg",
    r"\}.+\{thqxh",
    r"\}.+\{uiryi",
    r"\}.+\{vjszj",
    r"\}.+\{wktak",
    r"\}.+\{xlubl",
    r"\}.+\{ymvcm",
    r"\}.+\{znwdn",
    r"\}.+\{aoxeo",
    r"\}.+\{bpyfp",
    r"\}.+\{cqzgq",
    r"\}.+\{drahr",
    r"\}.+\{esbis",
]


def read_lines():
    filename_input = "735e2c6249eafe7f70c396fe4e808c1ce4a3c073238b66286fa0d59a6fd4b88c_puzzle"
    with open(filename_input) as f:
        content = f.read().strip()
        lines = content.splitlines()
    return lines


def find_horizontal(lines, searches):
    matches = []
    for line in lines:
        for key in searches:
            matches.extend(re.findall(key, line))
    return matches


def find_vertical(lines, searches):
    # width of the hori line is the new no. of vertical lines
    vert_length = len(lines[0])

    # transpose to get vertical lines
    vert_lines = [''] * vert_length
    for hori_no, content in enumerate(lines):
        for vert_no, ch in enumerate(list(content)):
            vert_lines[vert_no] += ch
            assert (hori_no+1) == len(vert_lines[vert_no])

    # print('\n'.join(vert_lines))
    return find_horizontal(vert_lines, searches)


def find_diagonal_left(lines, searches):
    # stagger the lines left first (top left diagonal)
    line_count = len(lines)
    for i in range(line_count):
        left = line_count - i
        right = i
        lines[i] = (' ' * left) + lines[i] + (' ' * right)
    return find_vertical(lines, searches)


def find_diagonal_right(lines, searches):
    # stagger the lines right first (top right diagonal)
    line_count = len(lines)
    for i in range(line_count):
        right = line_count - i
        left = i
        lines[i] = (' ' * left) + lines[i] + (' ' * right)
    return find_vertical(lines, searches)




if __name__ == '__main__':
    print("Horizontal")
    print(find_horizontal(read_lines(), search_words))
    print()

    print("Horizontal Reversed")
    print(find_horizontal(read_lines(), search_words_reversed))
    print()

    print("Vertical")
    print(find_vertical(read_lines(), search_words))
    print()

    print("Vertical Reversed")
    print(find_vertical(read_lines(), search_words_reversed))
    print()

    print("Diagonal Left")
    print(find_diagonal_left(read_lines(), search_words))
    print()

    print("Diagonal Left Reversed")
    print(find_diagonal_left(read_lines(), search_words_reversed))
    print()

    print("Diagonal Right")
    print(find_diagonal_right(read_lines(), search_words))
    print()

    print("Diagonal Right Reversed")
    print(find_diagonal_right(read_lines(), search_words_reversed))
    print()

