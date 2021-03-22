#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
nums = [69, 81, 30, 38, 9, 2, 47, 61, 32, 79, 1, 1, 1, 1, 1]
# nums = [1, 5, 11, 12][::-1]


def merge(nums, left, mid, right):
    leftSub = nums[left:mid + 1] + [np.inf]
    rightSub = nums[mid + 1:right + 1] + [np.inf]

    l, r = 0, 0

    for i in range(left, right + 1):
        if leftSub[l] <= rightSub[r]:
            nums[i] = leftSub[l]
            l += 1
        else:
            nums[i] = rightSub[r]
            r += 1

def msort(nums, left, right):
    if left < right:
        mid = int((right + left) / 2)
        msort(nums, left, mid)
        msort(nums, mid + 1, right)
        merge(nums, left, mid, right)


msort(nums, 0, len(nums) - 1)
print(nums)
