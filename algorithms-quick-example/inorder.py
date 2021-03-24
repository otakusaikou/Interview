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
def inorder(root):
    if root is None: return []
    ans = []
    q = []
    curr = root
    while curr or q:
        if curr is not None:
            q.append(curr)
            curr = curr.left
        else:
            curr = q.pop(-1)
            ans.append(curr.value)
            curr = curr.right
    return ans

print(inorder(root))
