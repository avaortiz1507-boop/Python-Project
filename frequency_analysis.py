#6 Include a short comment at the top of your file explaining what the program does
"""
This program takes survey responses to look for item frequencies, unique items, and the most common response.
"""

# 1 Start with a list of items that represents survey responses
survey_responses = ['apple', 'banana', 'apple', 'cherry', 'banana', 'apple']

# 2 Write a function that takes the list and returns a dictionary where keys are items and values are their frequencies
def count_frequencies(items):
    freq = {}
    for item in items:
        freq[item] = freq.get(item, 0) + 1
    return freq

# 3 Write a function that returns a set of unique items from the list
def get_unique_items(items):
    return set(items)

# 4 Write a function that returns the top N most frequent items using dictionary items and tuple unpacking
def top_n_frequent(items, n):
    freq = {}
    for item in items:
        freq[item] = freq.get(item, 0) + 1

    sorted_items = sorted(freq.items(), key=lambda pair: pair[1], reverse=True)
    top_n = []
    for item, count in sorted_items[:n]:
        top_n.append((item, count))

    return top_n

# 5 Print a clear, readable summary that shows frequencies, unique item count, and top results
def print_summary(items, n):
    freq = {}
    for item in items:
        freq[item] = freq.get(item, 0) + 1

    unique_count = len(freq)

    sorted_items = sorted(freq.items(), key=lambda pair: pair[1], reverse=True)

    top_n = [(item, count) for item, count in sorted_items[:n]]

    print("=== Summary ===")
    print("Frequencies:")
    for item, count in freq.items():
        print(f"  {item}: {count}")

    print(f"\nUnique item count: {unique_count}")

    print(f"\nTop {n} most frequent items:")
    for item, count in top_n:
        print(f"  {item}: {count}")


print_summary(survey_responses, 2)

    

