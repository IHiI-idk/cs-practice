def winner(names: list[str], scores: list[float]) -> str:
    return max(set(scores), key=scores.count)

def average(scores: list[float]) -> float:
    return sum(scores) / len(scores)

def ranking(names: list[str], scores: list[float]) -> list[str]:
    return [names[i] for i in sorted(range(len(names)), key=lambda i: scores[i], reverse=True)]

def above_average(names: list[str], scores: list[float]):
    avrg = average(scores)
    res = []
    for i in range(len(scores)):
        if scores[i] > avrg:
            res.append(names[i])
    return res







