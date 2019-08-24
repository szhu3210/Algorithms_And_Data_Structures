"""
Test of LC 952 solution
"""


import unittest


class TestLC952(unittest.TestCase):
    """
    Test class for LC 952 solution
    """

    def test_interview(self):
        """
        :return: None
        """
        from union_find.Practice_1_LC_952_Hard.practice_1_lc_952_hard import Interview
        interview = Interview()
        input_parm = [6, 15, 30, 49]
        output_result = 3
        self.assertEqual(interview.largest_component_size_1(input_parm), output_result)
        self.assertEqual(interview.largest_component_size_2(input_parm), output_result)
        self.assertEqual(interview.largest_component_size_3(input_parm), output_result)
        input_parm = [20, 50, 9, 63]
        output_result = 2
        self.assertEqual(interview.largest_component_size_1(input_parm), output_result)
        self.assertEqual(interview.largest_component_size_2(input_parm), output_result)
        self.assertEqual(interview.largest_component_size_3(input_parm), output_result)
        input_parm = [2, 3, 6, 7, 4, 12, 21, 39]
        output_result = 8
        self.assertEqual(interview.largest_component_size_1(input_parm), output_result)
        self.assertEqual(interview.largest_component_size_2(input_parm), output_result)
        self.assertEqual(interview.largest_component_size_3(input_parm), output_result)
