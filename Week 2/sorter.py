def sort_file(filename):

    with open(filename, "r") as file:
        lines = file.readlines()

    lines.sort()

    with open(filename, "w") as file:
        file.writelines(lines)