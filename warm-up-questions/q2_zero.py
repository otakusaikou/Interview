#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Question: https://www.codewars.com/kata/52f787eb172a8b4ae1000a34


# O(N)
def zero(N):
    fN = 0

    # Ignore 2 here as numbers of 2 is always greater than numbers of 5
    for i in range(1, N + 1):
        n = i
        while n % 5 == 0:
            n /= 5
            fN += 1

    return fN


print(zero(1000))
