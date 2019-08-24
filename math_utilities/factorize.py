"""
Factorize function module
"""


def factorize(number: int) -> list:
    """
    Return a list of all prime factors of an integer
    :param number: int
    :return: list
    """

    res = []
    prime_factor = 2  # prime factor start from 2
    while prime_factor * prime_factor <= number:
        if number % prime_factor == 0:
            while number % prime_factor == 0:
                number /= prime_factor
            res.append(prime_factor)
        prime_factor += 1
    if number > 1:
        res.append(int(number))
    return res


if __name__ == "__main__":
    for i in range(100):
        print(i, factorize(i))
