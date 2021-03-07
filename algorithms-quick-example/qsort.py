#!/usr/bin/env python
# -*- coding: utf-8 -*-


nums = [69, 81, 30, 38, 9, 2, 47, 61, 32, 79]
# nums = [1, 5, 11, 12][::-1]


def qsort(nums, left, right):
    if left >= right:
        return

    piv = nums[left]
    i = left
    j = right

    while i != j:
        # This while loop need to be run first
        while nums[j] > piv and i < j:
            j -= 1
        while nums[i] <= piv and i < j:
            i += 1

        if i != j:
            nums[i], nums[j] = nums[j], nums[i]

    nums[left], nums[i] = nums[i], nums[left]
    qsort(nums, left, i - 1)
    qsort(nums, i + 1, right)


qsort(nums, 0, len(nums) - 1)
print(nums)
