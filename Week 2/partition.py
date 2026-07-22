import os

def partition(mapped_data, reducers):

    os.makedirs("partitions", exist_ok=True)

    files = []

    for i in range(reducers):
        files.append(open(f"partitions/part-{i}.txt", "w"))

    for key, value in mapped_data:

        index = hash(key) % reducers

        files[index].write(f"{key} {value}\n")

    for file in files:
        file.close()