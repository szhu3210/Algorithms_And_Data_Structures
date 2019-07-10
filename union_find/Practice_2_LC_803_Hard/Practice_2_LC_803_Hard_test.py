import unittest


class TestLC803(unittest.TestCase):
    def test_interview(self):
        from union_find.Practice_2_LC_803_Hard.Practice_2_LC_803_Hard import Interview
        interview = Interview()

        i1 = [[1, 1, 1], [0, 1, 0], [0, 0, 0]]
        i2 = [[0, 2], [2, 0], [0, 1], [1, 2]]
        o = [0, 0, 1, 0]
        self.assertEqual(interview.hit_bricks(i1, i2), o)

        i1 = [[1, 0, 0, 0], [1, 1, 1, 0]]
        i2 = [[1, 0]]
        o = [2]
        self.assertEqual(interview.hit_bricks(i1, i2), o)

        i1 = [[1, 0, 0, 0], [1, 1, 0, 0]]
        i2 = [[1, 1], [1, 0]]
        o = [0, 0]
        self.assertEqual(interview.hit_bricks(i1, i2), o)
