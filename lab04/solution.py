def winner(names: list[str], scores: list[float]) -> str:
    if not scores: return ""
    return names[scores.index(max(scores))]

def average(scores: list[float]) -> float:
    if not scores:
        return 0.0
    return round((sum(scores) / len(scores)), 2)

def ranking(names: list[str], scores: list[float]) -> list[str]:
    return [names[i] for i in sorted(range(len(names)), key=lambda i: scores[i], reverse=True)]

def above_average(names: list[str], scores: list[float]):
    avrg = average(scores)
    res = []
    for i in range(len(scores)):
        if scores[i] > avrg:
            res.append(names[i])
    return res







