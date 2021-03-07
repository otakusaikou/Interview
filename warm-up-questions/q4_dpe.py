#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Question: https://www.codewars.com/kata/duplicate-encoder/python


# O(N)
def dpe(s):
    s = s.lower()
    d = {}

    for c in s:
        d[c] = d.get(c, 0) + 1

    ans = ""
    for c in s:
        if d[c] > 1:
            ans += ")"
        else:
            ans += "("

    print(ans)


dpe("din")
dpe("recede")
dpe("Success")
dpe("(( @")
