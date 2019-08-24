"""
Test for LC 803 solution
"""


import unittest


class TestLC803(unittest.TestCase):
    """
    Test class for LC 803 solution
    """

    def test_interview(self):
        """
        :return:
        """

        from union_find.Practice_2_LC_803_Hard.practice_2_lc_803_hard import hit_bricks

        input_parm1 = [[1, 1, 1], [0, 1, 0], [0, 0, 0]]
        input_parm2 = [[0, 2], [2, 0], [0, 1], [1, 2]]
        output_result = [0, 0, 1, 0]
        self.assertEqual(hit_bricks(input_parm1, input_parm2), output_result)

        input_parm1 = [[1, 0, 0, 0], [1, 1, 1, 0]]
        input_parm2 = [[1, 0]]
        output_result = [2]
        self.assertEqual(hit_bricks(input_parm1, input_parm2), output_result)

        input_parm1 = [[1, 0, 0, 0], [1, 1, 0, 0]]
        input_parm2 = [[1, 1], [1, 0]]
        output_result = [0, 0]
        self.assertEqual(hit_bricks(input_parm1, input_parm2), output_result)
