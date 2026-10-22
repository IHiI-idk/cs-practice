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

def common(first :list, second: list) -> list:
    common = []
    for a in first:
        if a in first and a in second:
            common.append(a)
    return sorted(common)

def only_in_first(first: list, second: list) -> list:
    only_in_second = []
    for a in first:
        for b in second:
            if a in first and b not in first and a not in second:
                only_in_second.append(a)
    return sorted(only_in_second)
