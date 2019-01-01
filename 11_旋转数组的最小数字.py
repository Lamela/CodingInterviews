def find_min(numbers):
    p1 = 0
    p2 = len(numbers) - 1
    p_mid = p1
    while numbers[p1] >= numbers[p2]:
        if p2 - p1 == 1:
            p_mid = p2
            break

        p_mid = (p1 + p2) // 2

        if numbers[p1] == numbers[p_mid] == numbers[p2]:
            return find_min_by_order(numbers[p1:p2+1])

        if numbers[p1] <= numbers[p_mid]:
            p1 = p_mid

        elif numbers[p2] >= numbers[p_mid]:
            p2 = p_mid

    return numbers[p_mid]


def find_min_by_order(numbers):
    min_value = numbers[0]
    for i in range(len(numbers)):
        if numbers[i] < min_value:
            min_value = numbers[i]

    return min_value


if __name__ == "__main__":
    print(find_min([3, 4, 5, 1, 2]))
    print(find_min([1, 1, 0, 1, 1]))
