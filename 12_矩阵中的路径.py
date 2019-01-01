def has_path(matrix, s):
    if not isinstance(matrix, list) or len(matrix) == 0 or len(matrix[0]) == 0 \
            or not isinstance(s, str) or len(s) == 0:
        return False

    rows = len(matrix)
    cols = len(matrix[0])
    for r in matrix:
        if not isinstance(r, list) or len(r) != cols:
            return False

    visited = [[False] * cols for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == s[0]:
                visited[i][j] = True
                found = has_path_recursively(matrix, s[1:], visited, (i, j))
                if found:
                    for r in visited:
                        print(r)
                    return True
                visited[i][j] = False

    return False


def has_path_recursively(matrix, s, visited, matrix_indices):
    if len(s) == 0:
        return True

    m_i, m_j = matrix_indices
    indices = []
    for delta in (-1, 1):
        if 0 <= m_i + delta < len(matrix) and not visited[m_i + delta][m_j]:
            indices.append((m_i + delta, m_j))

        if 0 <= m_j + delta < len(matrix[0]) and not visited[m_i][m_j + delta]:
            indices.append((m_i, m_j + delta))

    for next_m_i, next_m_j in indices:
        if matrix[next_m_i][next_m_j] == s[0]:
            visited[next_m_i][next_m_j] = True
            found = has_path_recursively(matrix, s[1:], visited, (next_m_i, next_m_j))
            if found:
                return True
            visited[next_m_i][next_m_j] = False

    return False


if __name__ == "__main__":
    matrix = [
        ["a", "b", "t", "g"],
        ["c", "f", "c", "s"],
        ["j", "d", "e", "h"]
    ]
    s = "bfce"
    print(has_path(matrix=matrix, s=s))