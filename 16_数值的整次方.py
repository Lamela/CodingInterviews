def power(base, exponent):
    """不考虑大数问题,0的0次方可为0可为1"""
    if base == 0 and exponent < 0:
        return None
    if base == 0 and exponent == 0:
        return 0

    unsigned_exponent = exponent if exponent >= 0 else abs(exponent)
    result = power_with_unsigned_exponent(base, unsigned_exponent)
    if exponent < 0:
        result = 1.0 / result

    return result


def power_with_unsigned_exponent(base, unsigned_exponent):
    if unsigned_exponent == 0:
        return 1
    if unsigned_exponent == 1:
        return base
    result = power_with_unsigned_exponent(base, unsigned_exponent >> 1)
    result *= result
    if unsigned_exponent % 2:
        result *= base

    return result


if __name__ == '__main__':
    print(power(0, 0))
    print(power(0, -1))
    print(power(4, -2))
    print(power(4, 2))