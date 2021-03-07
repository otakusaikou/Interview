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

# # Data2
# root = None
#
# # Data3
# root = node(2)
# root.left = node(8)
# root.right = node(9)
# current = root.left
# current.left = node(1)
# current.right = node(3)
# current = root.right
# current.left = node(4)
# current.right = node(5)


# O(V + E) (# of nodes + edges)
def dfs_trace(root):
    if not root:
        return None

    unvis = []
    vis = []
    unvis.append(root)
    while(unvis):
        current = unvis.pop()
        vis.append(current)
        if current.right:
            unvis.append(current.right)

        if current.left:
            unvis.append(current.left)
    return list(map(lambda n: n.value, vis))


print(dfs_trace(root))
