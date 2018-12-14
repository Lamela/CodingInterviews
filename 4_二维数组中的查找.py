def find_in_partially_sorted_matrix(matrix, number):
    """
    在从左到右，从上到下升序排列的矩阵中查找指定数字
    时间O(n), 空间O(1)
    :param matrix: List[List[int]]
    :param number: int
    :return: bool
    """
    if not isinstance(matrix, list) or len(matrix) < 1 \
            or not isinstance(matrix[0], list) or not isinstance(number, int):
        return False

    l, w = len(matrix), len(matrix[0])

    for i in range(l):
        if len(matrix[i]) != w:
            return False

        for j in range(w):
            if not isinstance(matrix[i][j], int):
                return False

    res = False
    i = 0
    j = w - 1
    while i < l and j >= 0:
        if matrix[i][j] > number:
            j -= 1
        elif matrix[i][j] < number:
            i += 1
        else:
            return True

    return res


if __name__ == "__main__":
        m = [[1, 2, 8, 9],
             [2, 4, 9, 12],
             [4, 7, 10, 13],
             [6, 8, 11, 15]]
        print(find_in_partially_sorted_matrix(m, 1))