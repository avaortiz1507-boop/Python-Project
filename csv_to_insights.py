from pathlib import Path
import csv
import json
from statistics_calculator import calculate_stats

csv_path = Path("C:/Users/avaor/Downloads/sample-superstore.csv")
results_path = Path(__file__).with_name("results.json")

try:
    with open(csv_path, mode='r', encoding='utf-8-sig', newline='') as file:
        csv_reader = csv.DictReader(file)
        profits = [float(row['Profit']) for row in csv_reader]
        stats = calculate_stats(profits)

        print(f"Minimum Profit: {stats['minimum']}")
        print(f"Maximum Profit: {stats['maximum']}")
        print(f"Average Profit: {stats['mean']}")
        print(f"Results saved to {results_path}")
        
        with open(results_path, "w") as json_file:
            json.dump(stats, json_file, indent=4)
except FileNotFoundError:
    print(f"File cannot be found: {csv_path}")
else:
    print("File read successfully.")

finally:
    print("Execution completed.")
