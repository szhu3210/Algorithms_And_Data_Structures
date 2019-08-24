"""

https://leetcode.com/problems/largest-component-size-by-common-factor/

Given a non-empty array of unique positive integers A, consider the following graph:

There are A.length nodes, labelled A[0] to A[A.length - 1];
There is an edge between A[i] and A[j] if and only if
    A[i] and A[j] share a common factor greater than 1.
Return the size of the largest connected component in the graph.

"""

from collections import Counter
from union_find.union_find_standard import UF
from math_utilities.factorize import factorize


class Interview:
    """
    Interview question of LeetCode 952
    """

    @staticmethod
    def largest_component_size_1(_a: list) -> int:
        """
        :param _a: List of integers
        :return: int
        """

        # factorize the int in A, put into list of b
        factor_list = list(map(factorize, _a))

        # find all connections and union node
        _uf = UF(len(_a))
        for i in range(len(_a)):
            for j in range(len(_a)):
                if set(factor_list[i]) & set(factor_list[j]):
                    _uf.union(i, j)

        # find the size of largest component
        return max(Counter(_uf.find(i) for i in range(len(_a))).values())

    @staticmethod
    def largest_component_size_2(_a: list) -> int:
        """
        :param _a: List of integers
        :return: int
        """

        # factorize the int in a, put into list of b
        factor_list = list(map(factorize, _a))

        # instead of connecting elements in a, we connect prime factors
        primes = list({p for factors in factor_list for p in factors})
        prime_to_index = {p: i for i, p in enumerate(primes)}
        _uf = UF(len(primes))
        for factors in factor_list:
            for factor in factors:
                _uf.union(prime_to_index[factors[0]], prime_to_index[factor])

        # find the size of largest component
        count = Counter([_uf.find(prime_to_index[factors[0]]) for factors in factor_list])
        return count.most_common(1)[0][1]

    @staticmethod
    def largest_component_size_3(_a: list) -> int:
        """
        :param _a: List of integers
        :return: int
        """

        # factorize the int in a, put into list of b
        factor_list = list(map(factorize, _a))

        # instead of connecting elements in a, we connect prime factors to the elements in a
        max_int = max(_a) + 1
        _uf = UF(max_int)
        for i, _ in enumerate(factor_list):
            for factor in factor_list[i]:
                _uf.union(_a[i], factor)

        # find the size of largest component
        count = Counter(_uf.find(num) for num in _a)

        return max(count.values())
