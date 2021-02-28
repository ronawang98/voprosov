import sys
"""
Description:

Given an array of integers, find the subset of non-adjacent elements with the maximum sum.
Calculate the sum of that subset.

It is possible that the maximum sum is 0, the case when all elements are negative.
"""


"""
Solution:

There are several things to consider:
- Gap between numbers in a subset:
    1) Skip 1 number  [pick, x, pick]
    2) Skip 2 numbers [pick, x, x, pick]
    3) Anything beyond a gap of 2 can use memoization to keep a running sum.
        - e.g. [2, -1, -1, -1, -1, 3, -1] => slide 2 to 3 (cha cha slide)
        - More on the next point...
- Subsets do not always have to span the entire array
    - A big clue is in the description that states that when all elements are negative, the maximum sum should be 0.
    - That is in the case of [a, -(b), -(c), d, e] where all letters represent positive numbers:
        - start:    [a, -(b), -(c), d, e]
        - index=0;  [a, -(b), -(c), d, e];  max(a, 0)
        - index=1;  [a, 0, -(c), d, e];     max(-(b), 0)
        - index=2;  [a, 0, a, d, e];        max(-(c), 0) + a
        - index=3;  [a, 0, a, d+a, e];      max(d, 0) + max(a, 0)
        - index=4;  [a, 0, a, d+a, e+a];    max(e, 0) + max(0, a)
        - end: Return max(d+a, e+a)
    - In any general case,
        - if index is 0 or 1: we take max(arr[index], 0)
        - If index is 2: we take max(arr[index], 0) + prevprev
        - If index is more than 2: we take max(curr, 0) + max(prevprev, prevprevprev)
- Edge cases:
    - array length 0: return 0
    - array length 1: return single element if positive, or else return 0

Time Complexity:
    - 0(n) where n is the length of the input array
    - It passes through the array once
Space Complexity:
    - O(1)
    - No extra space was used. Everything done in place.
"""

def maxSubsetSum(arr):
    if len(arr) == 0: return 0
    for i in range(len(arr)):
        arr[i] = max(arr[i], 0)
        if i == 2:
            arr[i] += arr[i-2]
        elif i > 2:
            arr[i] += max(arr[i-2], arr[i-3])
    return max(arr[-1], arr[-2]) if len(arr) > 1 else arr[-1]
