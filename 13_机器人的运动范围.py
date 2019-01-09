def moving_count(matrix, k):
    if k < 0 or len(matrix) <= 0 or len(matrix[0]) <= 0 or not isinstance(matrix, list):
        return 0

    rows = len(matrix)
    cols = len(matrix[0])

    for i in range(rows):
        if not isinstance(matrix[i], list) or len(matrix[i]) != cols:
            return 0

    visited = [[False] * cols for _ in range(rows)]

    matrix_indices = (0, 0)
    count = moving_count_recursively(matrix, k, matrix_indices, visited)

    return count


def moving_count_recursively(matrix, k, matrix_indices, visited):
    count = 0

    if check(matrix, k, matrix_indices, visited):
        visited[matrix_indices] = True
        count = 1
        for delta in (-1, 1):
            for m_i, m_j in matrix_indices:
                count += moving_count_recursively(matrix, k, (m_i + delta, m_j), visited)
                count += moving_count_recursively(matrix, k, (m_i, m_j + delta), visited)

    return count


def check(matrix, k , matrix_indices, visited):
    m_i, m_j = matrix_indices
    if not (0 <= m_i < len(matrix)) or not (0 <= m_j < len(matrix[0])) or \
            (sum_digit(m_i) + sum_digit(m_j) > k) or \
            visited[m_i][m_j]:
        return False
    return True


def sum_digit(x):
    sum = 0
    while x > 0:
        sum += x % 10
        x = x // 10
    return sum
