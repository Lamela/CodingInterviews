def number_of_1(n):
    """把一个整数减去1，再和原整数做与操作，会把原证书最右边的1变成0"""
    count = 0
    while n:
        count += 1
        n = n & (n - 1)

    return count


if __name__ == '__main__':
    print(number_of_1(9))