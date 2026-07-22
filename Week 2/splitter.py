import os

def split_input(input_file, output_folder="input", num_splits=4):
    # Create input folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Read all lines
    with open(input_file, "r") as file:
        lines = file.readlines()

    # Keep header separately
    header = lines[0]
    records = lines[1:]

    # Calculate records per split
    split_size = (len(records) + num_splits - 1) // num_splits

    # Create split files
    for i in range(num_splits):
        start = i * split_size
        end = start + split_size

        with open(f"{output_folder}/split_{i}.txt", "w") as out:
            out.write(header)
            out.writelines(records[start:end])

    print("Input file split successfully.")