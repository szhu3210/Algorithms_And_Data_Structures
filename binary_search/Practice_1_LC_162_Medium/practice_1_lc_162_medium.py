"""
https://leetcode.com/problems/find-peak-element/
"""


from typing import List


def find_peak(nums: List[int]) -> int:
    """
    nums: store positive values of height
    return: int, index of peak
    """
    len_nums = len(nums)
    if len_nums <= 3:
        return nums.index(max(nums))
    if nums[0] > nums[1]:
        return 0
    if nums[-1] > nums[-2]:
        return len_nums - 1

    l_bound, r_bound = 1, len_nums - 2
    while l_bound + 1 < r_bound:
        mid = l_bound + (r_bound - l_bound) // 2
        l_nb, r_nb = mid - 1, mid + 1
        if nums[l_nb] < nums[mid] > nums[r_nb]:
            return mid
        if nums[l_nb] < nums[mid]:
            l_bound = mid
        elif nums[l_nb] > nums[mid]:
            r_bound = mid
        else:
            raise ValueError('neighbouring values should not be the same')

    if nums[l_bound] > nums[r_bound]:
        return l_bound
    return r_bound
