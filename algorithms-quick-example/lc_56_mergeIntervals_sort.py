#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Solution:
    # O(nlogn)
    def sort(self, intervals, left, right):
        if left >= right:
            return

        i = left
        j = right
        piviot = intervals[left][0]

        while i != j:
            while intervals[j][0] > piviot and i < j:
                j -= 1
            while intervals[i][0] <= piviot and i < j:
                i += 1

            if i < j:
                intervals[i], intervals[j] = intervals[j], intervals[i]

        intervals[left], intervals[i] = intervals[i], intervals[left]
        self.sort(intervals, left, i - 1)
        self.sort(intervals, i + 1, right)

    # O(nlogn + n) = O(nlogn)
    def merge(self, intervals):
        self.sort(intervals, 0, len(intervals) - 1)
        st = 0
        i = 0
        j = 1

        ans = []

        while (j < len(intervals)):
            if intervals[j][0] <= intervals[i][1]:
                intervals[j][0] = intervals[i][0]
                intervals[j][1] = max(intervals[j][1], intervals[i][1])
                st += 1
            else:
                ans.append(intervals[i])
            i += 1
            j += 1

        ans.append(intervals[j - 1])

        return ans


solution = Solution()
intervals = [[2, 3], [2, 2], [3, 3], [1, 3], [5, 7], [2, 2], [4, 6]]
# intervals = [[1,3],[5,9],[11,17],[12,13]]
print(solution.merge(intervals))
