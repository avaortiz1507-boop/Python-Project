from pathlib import Path
import csv

csv_path = Path("C:/Users/avaor/Downloads/sample-superstore.csv")

with open(csv_path, mode='r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        print(row)