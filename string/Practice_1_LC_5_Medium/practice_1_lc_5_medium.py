"""
LeetCode Problem # 5
"""


def longest_palindrome(input_string: str) -> str:
    """
    :param input_string: str
    :return: str
    """
    input_string_length = len(input_string)
    res = [1, 0, 0]

    def expand(left_bound, right_bound):
        """
        :param left_bound: left index
        :param right_bound: right index
        :return: None
        """
        while (left_bound - 1 >= 0 and right_bound + 1 < input_string_length and
               input_string[left_bound - 1] == input_string[right_bound + 1]):
            left_bound -= 1
            right_bound += 1
        length = right_bound - left_bound + 1
        if length > res[0]:
            res[:] = [length, left_bound, right_bound]

    for character in range(input_string_length):
        i = j = character
        expand(i, j)
        if (
                character + 1 < input_string_length and
                input_string[character] == input_string[character + 1]
        ):
            i, j = character, character + 1
            expand(i, j)

    _, i, j = res
    return input_string[i: j + 1]
