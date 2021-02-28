import sys
"""
Description:

You can perform the following operations on the string a:
    - Capitalize zero or more of a's lowercase letters
    - Delete all of the remaining lowercase letters in a

Determine if it's possible to make a equal to b as described.
e.g. a = AbcDE, b = ABDE => convert b to B and delete c => True
     a = AbcDE, b = AFDE => invalid => False
"""


"""
Solution:

Things to consider:
- Overlapping cases
    - In the small case a = "fF", b = "F"
        - If the first "f" was converted to "F" to match b, this would fail.
            -> a = "fF" -> "FF" != b
        - The correct way to do this is to drop "f".
            -> a = "fF" -> "F" == b

Strategies:
1) Keep a pointer in each string and compare and see if they match or not
    - Con: Overlapping cases, we need to be able to look beyond the current character
        - Doesn't actually solve all cases
2) Create a 2D array to keep track of if the characters match, in an incremental way
    - Time complexity: O(len(a) * len(b))
    - Space complexity: O(len(a) * len(b))
    1. Initialize all elements in 2D array to False
    2. Iterate over each relevant square in the 2D array, only changing square to True if:
        i.   Current element in a is lower case,
        ii.  Uppercase of current element in a matches current element in b.
        iii. and the running solution is True.
    3. Return the last element, which is the running solution.
"""
def abbreviation(a, b):
    if len(a) < len(b):
        return False
    dp = [[False for i in range(len(b)+1)] for j in range(len(a)+1)]
    dp[0][0] = True
    for i in range(1, len(a)+1):
        if a[i-1].islower():
            dp[i][0] = True

    for i in range(1, len(a)+1):
        for j in range(1, min(len(b)+1, i+1)):
            if a[i-1].islower():
                dp[i][j] = dp[i][j] or dp[i-1][j]
            if a[i-1].upper() == b[j-1]:
                dp[i][j] = dp[i][j] or dp[i-1][j-1]
    return dp[-1][-1]
