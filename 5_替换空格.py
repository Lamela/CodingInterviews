def replace_space(s):
    """
    在原字符串上将空格替换为%20字符
    时间O(n), 空间O(1)
    :param s: str
    :return: str
    """
    if not isinstance(s, str) or len(s) < 1:
        return None

    s = list(s)
    p1 = len(s) - 1
    for ch in s:
        if ch == ' ':
            s.append(None)
            s.append(None)

    p2 = len(s) - 1
    while p1 != p2:
        if s[p1] == ' ':
            s[p2-2:p2+1] = '%20'
            p2 -= 3
        else:
            s[p2] = s[p1]
            p2 -= 1
        p1 -= 1

    return "".join(s)


if __name__ == "__main__":
    print(replace_space("we are friend"))