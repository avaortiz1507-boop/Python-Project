
import statistics


def calculate_stats(numbers):
    minimum = min(numbers)
    maximum = max(numbers)
    mean = statistics.mean(numbers)

    return {
        "minimum": minimum,
        "maximum": maximum,
        "mean": mean
    }
