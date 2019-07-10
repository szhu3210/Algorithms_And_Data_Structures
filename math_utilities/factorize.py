def factorize(n: int) -> list:
    """
    Return a list of all prime factors of an integer
    :param n: int
    :return: list
    """

    res = []
    p = 2  # prime factor start from 2
    while p * p <= n:
        if n % p == 0:
            while n % p == 0:
                n /= p
            res.append(p)
        p += 1
    if n > 1:
        res.append(int(n))
    return res


if __name__ == "__main__":
    for i in range(100):
        print(i, factorize(i))
