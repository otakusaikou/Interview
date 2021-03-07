#!/usr/bin/env python
# -*- coding: utf-8 -*-

s = "ABCD"
choosed = [0] * len(s)
ans = ""


def bk(n):
    global ans

    if len(ans) == len(s):
        print(ans)
        return

    for i in range(n):
        ans += s[i]
        choosed[i] = 1
        bk(n)
        ans = ans[:-1]
        choosed[i] = 0


bk(4)
