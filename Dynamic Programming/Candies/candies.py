import sys
"""
Description:

Given an array of marks according to children, give minimum total amount of candy based on criteria:
- At least 1 candy per child
- When 2 children 'a' and 'b' are next each other i.e. [..., 'a', 'b', ...]
    - If 'a' > 'b': give 'a' more candy
    - If 'a' < 'b': give 'b' more candy
    - If 'a' == 'b': any arrangement
"""

"""
Solution:

Things to consider:
- Mark direction can shift negatively when the previous candy allocation was 1.
    - Allocations will not always start at 1

- Allocations can jump more than 1 amount each time
    - e.g. [5, 3, 1, 6, 6, 2, 1] -> 15
        - Allocation: [3, 2, 1, 4, 3, 2, 1] (1 to 4 between indices 2 & 3)
    - e.g. [2, 4, 5, 2] -> 7
        - Allocation: [1, 2, 3, 1] (3 to 1 between indices 2 & 3)

1) Iterate through the array and deal with descending chain of marks accordingly (Time Limit Exceeded)
    a) If increasing in array, increment in solution
    b) If decreasing in array, traverse backwards until it hits:
        i)   The start of the array
        ii)  2 array elements in non-descending order
        iii) 2 solution elements in ascending order
    - Time complexity: Worst case O(n^2) when all elements are descending, step b)
        will traverse backwards until it hits the start of the array every time.
2) Optimized solution:
    - This optimizes part b) of the first solution, by only requiring one backwards pass, rather than worst case n passes.
    a) Do a forward pass incrementing solution if increasing in array
    b) Do a backward pass incrementing solution if decreasing in array but increasing in solution
    - Time complexity: O(2*n) = O(n)

Space complexity: O(n) for both solutions.
"""
def candies(arr):
    n = len(arr)
    sol = [1] * n
    for i in range(n-1):
        if arr[i+1] > arr[i]:
            sol[i+1] = sol[i] + 1
        else:
            temp = i + 1
            while temp > 0 and arr[temp-1] > arr[temp] and sol[temp-1] <= sol[temp]:
                sol[temp-1] += 1
                temp -= 1
    return sum(sol)

def candies_optimized(arr):
    n = len(arr)
    sol = [1] * n
    for i in range(n-1):
        if arr[i+1] > arr[i]:
            sol[i+1] = sol[i] + 1
    for i in range(n-1, 0, -1):
        if arr[i-1] > arr[i] and sol[i-1] <= sol[i]:
            sol[i-1] = sol[i] + 1
    return sum(sol)
