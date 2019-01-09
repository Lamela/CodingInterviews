def fibonacci_iter(n):
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


def fibonacci_recur(n):
    if n < 2:
        return n

    return fibonacci_recur(n - 1) + fibonacci_recur(n - 2)


if __name__ == "__main__":
    print(fibonacci_iter(0))
    print(fibonacci_iter(1))
    print(fibonacci_iter(2))
    print(fibonacci_iter(20))
    print(fibonacci_recur(0))
    print(fibonacci_recur(1))
    print(fibonacci_recur(2))
    print(fibonacci_recur(20))