import csv
from statistics import mean


def substitute_missing_values(values):
    for i, value in enumerate(values):
        if value != '':
            values[i] = float(value)
        else:
            closest_values = (float(next((values[j] for j in range(i - 1, -1, -1) if values[j] != ''), 0)),
                              float(next((values[j] for j in range(i + 1, len(values)) if values[j] != ''), 0)))
            values[i] = mean(closest_values)
    return values


with open("glt.csv") as file:
    next(csv.reader(file))
    dataset = [line for line in csv.reader(file)]

average_temperature_processed = substitute_missing_values([line[1] for line in dataset])


