#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Reference: https://leetcode.com/problems/rotting-oranges/

grid = [[2, 1, 1],
        [1, 1, 1],
        [0, 1, 2]]


def getRottenCoords(grid):
    rottenCoords = []
    freshOrange = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == 2:
                rottenCoords.append((r, c))
            elif grid[r][c] == 1:
                freshOrange += 1
    return rottenCoords, freshOrange


def bfs(grid, rottenCoords, freshOrange):
    step = 0
    nrow = len(grid)
    ncol = len(grid[0])
    while rottenCoords:
        print("Current rotten oranges: " + str(rottenCoords))
        for _ in range(len(rottenCoords)):
            cr, cc = rottenCoords.pop(0)
            for tr, tc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                # Skip coordinates out of boundary
                if (cr + tr) < 0 or (cr + tr) >= nrow or \
                        (cc + tc) < 0 or (cc + tc) >= ncol:
                    continue

                # Skip non fresh orange
                if grid[cr + tr][cc + tc] != 1:
                    continue

                grid[cr + tr][cc + tc] = 2
                freshOrange -= 1
                rottenCoords.append((cr + tr, cc + tc))
                print("Orange (%d, %d) becomes rotten" % (cr + tr, cc + tc))
        step += 1
        print("After step %d: %s, freshOrange: %d" %
              (step, rottenCoords, freshOrange))
        if freshOrange == 0:
            return step
    return -1


rottenCoords, freshOrange = getRottenCoords(grid)
print("Step required: %d (-1 means there are fresh oranges remained)" %
      bfs(grid, rottenCoords, freshOrange))
