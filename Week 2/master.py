import os

from mapper import mapper
from partition import partition
from sorter import sort_file
from reducer import reducer

REDUCERS = 4
with open("input/input.txt", "r") as file:
    lines = file.readlines()

# Skip Header
records = lines[1:]

# Mapper
mapped = mapper(records)

# Partition
partition(mapped, REDUCERS)

# Sort
for i in range(REDUCERS):

    filename = f"partitions/part-{i}.txt"

    sort_file(filename)

# Reduce
final = {}

for i in range(REDUCERS):

    filename = f"partitions/part-{i}.txt"

    result = reducer(filename)

    for key, value in result.items():

        final[key] = final.get(key, 0) + value

# Output Folder
os.makedirs("output", exist_ok=True)

# Save Output
with open("output/result.txt", "w") as file:

    file.write("Subject Count\n")

    for key in sorted(final):

        file.write(f"{key} {final[key]}\n")

print("========== MapReduce Completed ==========")

for key in sorted(final):

    print(key, ":", final[key])

print("\nOutput saved in output/result.txt")