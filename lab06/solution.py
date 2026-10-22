def count_items(values) -> dict:
    counts = {}
    for value in values:
        counts[value] = counts.get(value, 0) + 1
    return counts

def unique_sorted(values) -> list:
    unique = []
    sorted_values = sorted(set(values))
    for v in sorted_values:
        unique.append(v)
    list(unique)
    return unique

