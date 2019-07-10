import unittest


class TestLC952(unittest.TestCase):
    def test_interview(self):
        from union_find.Practice_1_LC_952_Hard.Practice_1_LC_952_Hard import Interview
        interview = Interview()
        i = [6, 15, 30, 49]
        o = 3
        self.assertEqual(interview.largest_component_size_1(i), o)
        self.assertEqual(interview.largest_component_size_2(i), o)
        self.assertEqual(interview.largest_component_size_3(i), o)
        i = [20, 50, 9, 63]
        o = 2
        self.assertEqual(interview.largest_component_size_1(i), o)
        self.assertEqual(interview.largest_component_size_2(i), o)
        self.assertEqual(interview.largest_component_size_3(i), o)
        i = [2, 3, 6, 7, 4, 12, 21, 39]
        o = 8
        self.assertEqual(interview.largest_component_size_1(i), o)
        self.assertEqual(interview.largest_component_size_2(i), o)
        self.assertEqual(interview.largest_component_size_3(i), o)
