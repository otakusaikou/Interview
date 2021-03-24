#!/usr/bin/env python
# -*- coding: utf-8 -*-


class node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.value = val


# Data1
root = node(1)
root.left = node(8)
root.right = node(4)
current = root.left
current.right = node(3)
current = root.right
current.right = node(5)
current = current.right
current.right = node(7)

# Data2
root = None

# Data3
root = node(2)
root.left = node(8)
root.right = node(9)
current = root.left
current.left = node(1)
current.right = node(3)
current = root.right
current.left = node(4)
current.right = node(5)

# O(N)
def dfs_trace(root):
    if root is None: return []
    ans = []
    q = [root]
    while q:
        for _ in range(len(q)):
            curr = q.pop(-1)
            ans.append(curr.value)
            if curr.right is not None:
                q.append(curr.right)
            if curr.left is not None:
                q.append(curr.left)
    return ans

print(dfs_trace(root))
