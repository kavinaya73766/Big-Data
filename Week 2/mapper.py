def mapper(lines):

    mapped = []

    for line in lines:

        data = line.strip().split()

        if len(data) == 3:

            subject = data[2]

            mapped.append((subject, 1))

    return mapped