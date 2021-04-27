#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Reference: https://leetcode.com/problems/number-of-islands/

grid = [["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "1"],
        ["0", "0", "1", "0", "1"]]


def dfs(grid, startCoords):
    sr, sc = startCoords
    if grid[sr][sc] in ["0", "2"]:
        return 0

    nrow = len(grid)
    ncol = len(grid[0])
    queue = [(sr, sc)]
    area = 0
    while queue:
        print("Current queue: " + str(queue))
        cr, cc = queue.pop(-1)
        grid[cr][cc] = "2"
        for tr, tc in [(-1, 0), (0, 1), (1, 0), (0, -1)][::-1]:
            # Skip coordinates out of boundary
            if (cr + tr) < 0 or (cr + tr) >= nrow or \
                    (cc + tc) < 0 or (cc + tc) >= ncol:
                continue

            # Skip non island cell
            if grid[cr + tr][cc + tc] != "1":
                continue

            grid[cr + tr][cc + tc] = "3"
            queue.append((cr + tr, cc + tc))
        area += 1
        print("After movement %s" % queue)
        for row in grid:
            print(row)
        print("Island area: %d" % area)
        print()
    return 1


def dfs_recursive(grid, startCoords, area):
    sr, sc = startCoords
    nrow = len(grid)
    ncol = len(grid[0])
    if sr < 0 or sr >= nrow or sc < 0 or sc >= ncol:
        return 1, area

    if grid[sr][sc] != "1":
        return 1, area

    grid[sr][sc] = "3"
    up, area = dfs_recursive(grid, (sr - 1, sc), area)
    right, area = dfs_recursive(grid, (sr, sc + 1), area)
    down, area = dfs_recursive(grid, (sr + 1, sc), area)
    left, area = dfs_recursive(grid, (sr, sc - 1), area)

    if up and right and down and left:
        grid[sr][sc] = "2"
        print("After movement")
        for row in grid:
            print(row)
        print("Island area: %d" % (area + 1))
        print()

        return 1, area + 1
    return -1, area


# While solution
# ans = 0
# for r in range(len(grid)):
#     for c in range(len(grid[0])):
#         ans += dfs(grid, (r, c))
# print("Total island count: %d" % ans)

# Recursive solution
ans = area = 0
for r in range(len(grid)):
    for c in range(len(grid[0])):
        if grid[r][c] == "1":
            result = dfs_recursive(grid, (r, c), area)
            ans += result[0]
            area = result[1]

print("Total island count: %d" % ans)
