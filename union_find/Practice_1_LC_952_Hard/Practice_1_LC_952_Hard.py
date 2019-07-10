"""

https://leetcode.com/problems/largest-component-size-by-common-factor/

Given a non-empty array of unique positive integers A, consider the following graph:

There are A.length nodes, labelled A[0] to A[A.length - 1];
There is an edge between A[i] and A[j] if and only if A[i] and A[j] share a common factor greater than 1.
Return the size of the largest connected component in the graph.

"""

from collections import Counter

from union_find.union_find_standard import UF
from math_utilities.factorize import factorize


class Interview:

    @staticmethod
    def largest_component_size_1(a: list) -> int:
        # factorize the int in A, put into list of b
        b = list(map(factorize, a))
        # find all connections and union node
        uf = UF(len(a))
        for i in range(len(a)):
            for j in range(len(a)):
                # if i == j:
                #     continue
                if set(b[i]) & set(b[j]):
                    uf.union(i, j)
        # find the size of largest component
        return max(Counter(uf.find(i) for i in range(len(a))).values())

    @staticmethod
    def largest_component_size_2(a: list) -> int:
        # factorize the int in a, put into list of b
        b = list(map(factorize, a))
        # instead of connecting elements in a, we connect prime factors
        primes = list({p for factors in b for p in factors})
        prime_to_index = {p: i for i, p in enumerate(primes)}
        uf = UF(len(primes))
        for factors in b:
            for x in factors:
                uf.union(prime_to_index[factors[0]], prime_to_index[x])
        # find the size of largest component
        count = Counter([uf.find(prime_to_index[factors[0]]) for factors in b])
        return count.most_common(1)[0][1]

    @staticmethod
    def largest_component_size_3(a: list) -> int:
        # factorize the int in a, put into list of b
        b = list(map(factorize, a))
        # instead of connecting elements in a, we connect prime factors to the elements in a
        m = max(a)+1
        uf = UF(m)
        for i in range(len(b)):
            for x in b[i]:
                uf.union(a[i], x)
        # find the size of largest component
        count = Counter(uf.find(x) for x in a)
        return max(count.values())
