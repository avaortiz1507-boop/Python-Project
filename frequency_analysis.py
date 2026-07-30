
# This program takes survey responses to look for item frequencies, unique items, and the most common responses.

from typing import Dict, List, Set


survey_responses: List[str] = ['apple', 'banana', 'apple', 'cherry', 'banana', 'apple']

def count_frequencies(items: List[str]) -> Dict[str, int]:
    freq: Dict[str, int] = {}
    for item in items:
        freq[item] = freq.get(item, 0) + 1
    return freq

def get_unique_items(items: List[str]) -> Set[str]:
    return set(items)

def top_n_frequent(freq: Dict[str, int], n):
    sorted_items = sorted(freq.items(), key=lambda pair: pair[1], reverse=True)
    return sorted_items[:n]

def print_summary(items, n):
    freq: Dict[str, int] = count_frequencies(items)
    unique_items = get_unique_items(items)
    top_n = top_n_frequent(freq, n)

    print(" Summary ")
    print("Frequencies:")
    for item, count in freq.items():
        print(f"  {item}: {count}")

    print(f"\nUnique item count: {len(unique_items)}")

    print(f"\nTop {n} most frequent items:")
    for item, count in top_n:
        print(f"  {item}: {count}")


# main check
if __name__ == "main":
    print_summary(survey_responses, 2)


    

