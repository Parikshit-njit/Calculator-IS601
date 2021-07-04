import csv


def read_csv(filename):
    test_cases = []
    with open(filename, "r") as file:
        next(file)
        reader = csv.reader(file);
        for row in reader:
            test_cases.append(row)
    return test_cases