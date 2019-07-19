class Solution:
    def __init__(self):
        self.mem = {}

    def removeBoxes(self, boxes) -> int:

        boxes = tuple(boxes)

        l = len(boxes)
        if l == 0:
            self.mem[boxes] = 0
            return 0
        if l == 1:
            self.mem[boxes] = 1
            return 1

        if boxes in self.mem:
            return self.mem[boxes]

        first = boxes[0]
        i = 0
        while i < l and boxes[i] == first:
            i += 1

        gain = i * i + self.removeBoxes(boxes[i:])
        for j in range(i + 1, l):
            if boxes[j] == first:
                p = self.removeBoxes(boxes[i: j])
                q = self.removeBoxes(boxes[:i] + boxes[j:])
                gain = max(gain, p + q)

        self.mem[boxes] = gain
        return gain
