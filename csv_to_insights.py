from pathlib import Path
import csv

csv_path = Path("C:/Users/avaor/Downloads/sample-superstore.csv")

try:
    with open(csv_path, mode='r') as file:
        csv_reader = csv.DictReader(file)
        profits = [float(row['Profit']) for row in csv_reader]
        for profit in profits:
            print(profit)
except FileNotFoundError:
    print(f"File cannot be found: {csv_path}")
    