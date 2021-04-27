#!/usr/bin/env python
# -*- coding: utf-8 -*-

nums = [69, 81, 30, 38, 9, 2, 47, 61, 32, 79, 1, 1, 1, 1]

#                      69
#               81            30
#            38     9       2    47
#          61  32 79 1     1 1  1
#
#       0  1  2  3  4  5  6  7  8  9  10  11  12  13
#       69 81 30 38 9  2  47 61 32 79 1   1   1   1


# O(logN)
def maxHeapify(nums, root_idx, length):
    left_idx = (root_idx * 2) + 1
    right_idx = (root_idx * 2) + 2
    largest_idx = root_idx

    if left_idx < length and nums[root_idx] < nums[left_idx]:
        largest_idx = left_idx

    if right_idx < length and nums[largest_idx] < nums[right_idx]:
        largest_idx = right_idx

    if largest_idx != root_idx:
        nums[root_idx], nums[largest_idx] = nums[largest_idx], nums[root_idx]
        maxHeapify(nums, largest_idx, length)


# O(logN)
def minHeapify(nums, root_idx, length):
    left_idx = (root_idx * 2) + 1
    right_idx = (root_idx * 2) + 2
    smallest_idx = root_idx

    if left_idx < length and nums[root_idx] > nums[left_idx]:
        smallest_idx = left_idx

    if right_idx < length and nums[smallest_idx] > nums[right_idx]:
        smallest_idx = right_idx

    if smallest_idx != root_idx:
        nums[root_idx], nums[smallest_idx] = nums[smallest_idx], nums[root_idx]
        minHeapify(nums, smallest_idx, length)


# O(NlogN)
def heapSort(heap, length):
    # O(N)
    while length > 1:
        # Move maximum node to last position
        heap[0], heap[length - 1] = heap[length - 1], heap[0]

        # Ignore last element (length - 1)
        length -= 1

        # Update heap to fulfill maxheap rule, O(logN)
        maxHeapify(heap, 0, length)


# O(NlogN)
def heapSortReverse(heap, length):
    # O(N)
    while length > 1:
        # Move minimun node to last position
        heap[0], heap[length - 1] = heap[length - 1], heap[0]

        # Ignore last element (length - 1)
        length -= 1

        # Update heap to fulfill minheap rule, O(logN)
        minHeapify(heap, 0, length)


# O(logN)
def extractMin(minHeap):
    if len(minHeap) == 0:
        return None

    minEle = minHeap[0]
    minHeap[0] = minHeap[-1]
    minHeap.pop(-1)
    minHeapify(minHeap, 0, len(minHeap))
    return minEle


# Build maxHeap: O(NlogN)
# for i in range((len(nums) // 2) - 1, -1, -1):
#    maxHeapify(nums, i, len(nums))
# heapSort(nums, len(nums))
# print(nums)

# Build minHeap: O(NlogN)
for i in range((len(nums) // 2) - 1, -1, -1):
    minHeapify(nums, i, len(nums))
print(nums)

for i in range(len(nums)):
    print(extractMin(nums))
heapSortReverse(nums, len(nums))
print(nums)
