#!/usr/bin/env python
# -*- coding: utf-8 -*-


def binSerach(l, target):
    lo = 0
    hi = len(l) - 1
    mid = int((lo + hi) / 2)
    while lo <= hi:
        if l[mid] < target:
            lo = mid + 1
        elif l[mid] > target:
            hi = mid - 1
        else:
            return mid
        mid = int((lo + hi) / 2)
    return mid


li = [1, 10, 23]

result = binSerach(li, 13)
print(result, li[result])
