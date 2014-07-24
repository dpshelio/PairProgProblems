def separateIn2(infile, outfile):
    from random import shuffle

    with open(infile, 'r') as f:
        lines = f.readlines()

    llines = len(lines)
    common_part = lines[2 * llines / 3 :]
    part1 = lines[:llines / 3] + common_part
    part2 = lines[llines / 3 : 2 * llines / 3] + common_part
    shuffle(part1)
    shuffle(part2)
    with open(outfile + '1.txt', 'w') as f:
        f.writelines(part1)
    with open(outfile + '2.txt', 'w') as f:
        f.writelines(part2)

if __name__ == "__main__":
    separateIn2('names.txt', 'names_')
