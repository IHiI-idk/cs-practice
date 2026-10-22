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
    only_in_first_list = []
    for a in first:
        if a not in second and a not in only_in_first_list:
            only_in_first_list.append(a)
    return sorted(only_in_first_list)