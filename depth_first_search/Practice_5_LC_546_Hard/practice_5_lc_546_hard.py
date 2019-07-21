"""
LC Problem No. 546
"""


from typing import Tuple


class Solution:  # pylint: disable=too-few-public-methods

    """
    Solution of LC 546
    """

    def __init__(self):
        """
        mem is used to cache the intermediate results
        """
        self.mem = {}

    def remove_boxes(self, boxes: Tuple[int]) -> int:
        """
        :param boxes: list of integers indicating the color of box
        :return: maximum gain by removing boxes wisely
        """

        boxes = tuple(boxes)

        box_len = len(boxes)
        if box_len == 0:
            self.mem[boxes] = 0
            return 0
        if box_len == 1:
            self.mem[boxes] = 1
            return 1

        if boxes in self.mem:
            return self.mem[boxes]

        first = boxes[0]
        i = 0
        while i < box_len and boxes[i] == first:
            i += 1

        gain = i * i + self.remove_boxes(boxes[i:])
        for j in range(i + 1, box_len):
            if boxes[j] == first:
                previous_step = self.remove_boxes(boxes[i: j])
                cur_step = self.remove_boxes(boxes[:i] + boxes[j:])
                gain = max(gain, previous_step + cur_step)

        self.mem[boxes] = gain
        return gain
