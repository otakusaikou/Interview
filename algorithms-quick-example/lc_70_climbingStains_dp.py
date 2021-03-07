#!/usr/bin/env python
# -*- coding: utf-8 -*-


# O(N)
class Solution:
    def climbStairs(self, n):
        if n == 1:
            return 1

        dp = [1] * (n - 1)

        for i in range(n - 1):
            if i == 0:
                dp[i] = 2
            elif i == 1:
                dp[i] = 3
            else:
                dp[i] = dp[i - 1] + dp[i - 2]
        return dp[-1]

sol = Solution()
print(sol.climbStairs(10))
