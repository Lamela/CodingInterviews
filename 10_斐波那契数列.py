def fibonacci(n):
    """
    题目一 求斐波那契数列的第n项
    时间O(n)
    :param n: int
    :return: int
    """
    res = [0, 1]
    if n < 2:
        return res[n]

    s1 = 1
    s2 = 0
    for i in range(2, n+1):
        s = s1 + s2

        s2 = s1
        s1 = s

    return s


if __name__ == "__main__":
    print(fibonacci(0))
    print(fibonacci(1))
    print(fibonacci(2))
    print(fibonacci(20))