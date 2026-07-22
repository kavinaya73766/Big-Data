from collections import defaultdict

def reducer(filename):

    result = defaultdict(int)

    with open(filename, "r") as file:

        for line in file:

            key, value = line.strip().split()

            result[key] += int(value)

    return result