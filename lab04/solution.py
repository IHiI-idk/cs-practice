def winner(names: list[str], scores: list[float]):
    return max(set(scores), key=scores.count)

def average(scores: list[float]):
    return sum(scores) / len(scores)







