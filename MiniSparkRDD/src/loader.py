# src/loader.py


import csv


def load_csv(file_path):

    data = []


    with open(
        file_path,
        "r",
        encoding="utf-8"
    ) as file:


        reader = csv.DictReader(file)


        for row in reader:

            data.append(row)


    return data