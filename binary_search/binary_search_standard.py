"""
九章算法的二分模版
"""


def find(nums, target, left=True):
    """
    Find first index of target in nums (sorted), return -1 if not found
    :param nums:
    :param target:
    :param left: True -> when there are duplicated nums, return the first occurrence
    :return: index of target
    """
    if not nums:
        return -1
    start, end = 0, len(nums) - 1
    while start + 1 < end:
        """
        final state will have start and end (two elements) 
        range (from start to end) is guaranteed to be shortened in each loop
        """
        mid = start + (start - end) // 2
        if nums[mid] == target:
            if left:
                end = mid
            else:
                start = mid
        elif nums[mid] < target:
            start = mid  # or start = mid - 1
        else:
            end = mid  # or end = mid + 1
    if nums[start] == target:
        return start
    if nums[end] == target:
        return end
    return -1
