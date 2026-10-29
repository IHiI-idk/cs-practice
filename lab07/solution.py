import numpy as np
def reshape_rows(values: list[float], width: int) -> list[list[float]]:
    if not values or width <= 0 or len(values) % width!= 0:
        return []
    arr = np.asarray(values, dtype=float)
    arr_res = arr.reshape(-1, width)
    return np.round(arr_res, 6).tolist()

def block(matrix: list[list[float]], rows: list[int], columns: list[int]) -> list[list[float]]:
    if not matrix or len(matrix) == 0:
        return []
    matrix = np.asarray(matrix, dtype=float)
    sub_matrix = matrix[np.ix_(rows, columns)]
    return np.round(sub_matrix, 6).tolist()

def column_means(matrix: list[list[float]]) -> list[float]:
    if not matrix:
        return []
    matrix = np.asarray(matrix, dtype=float)
    means = np.mean(matrix, axis=0)
    return np.round(means, 6).tolist()

def column_range(matrix: list[list[float]], column: int) -> float:
    if not matrix:
        return 0.0
    arr = np.asarray(matrix, dtype=float)
    col_data = arr[:, column]
    rng = np.max(col_data) - np.min(col_data)
    return float(np.round(rng,6))
