#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Question: https://www.codewars.com/kata/52774a314c2333f0a7000688


# O(N)
def vp(s):
    if not s:
        return False

    op = 0
    cl = 0
    for c in s:
        if c == "(":
            op += 1
        else:
            cl += 1

        if cl > op:
            return False

        if op >= 1 and cl >= 1:
            op -= 1
            cl -= 1
    return (op + cl) == 0


s = "(((())))"
print(s, vp(s), "True")

s = "("
print(s, vp(s), "False")

s = ")"
print(s, vp(s), "False")

s = ""
print(s, vp(s), "False")

s = "(())((()())())"
print(s, vp(s), "True")

s = ")(()))"
print(s, vp(s), "False")
