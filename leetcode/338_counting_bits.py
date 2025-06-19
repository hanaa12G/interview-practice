"""
Given an integer n, return an array ans of length n + 1 such that for each i 
(0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

 

Example 1:

Input: n = 2
Output: [0,1,1]
Explanation:
0 --> 0
1 --> 1
2 --> 10

Example 2:

Input: n = 5
Output: [0,1,1,2,1,2]
Explanation:
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101

 

Constraints:

    0 <= n <= 105

 

Follow up:

    It is very easy to come up with a solution with a runtime of O(n log n).
    Can you do it in linear time O(n) and possibly in a single pass?
    Can you do it without using any built-in function (i.e., like 
    __builtin_popcount in C++)?

"""


import math

class Solution:
    """
    # Idea

    1 thing I notice is that we can have some ways to calculate number n+1 if we
    already have bit count of number n. But the bit number can be flipped

    Number of bits increase if n is exponent of 2


    0 -> 0 (1, 0) ------------------|
    1 -> 1 (1, 1)                   |
                                    |
    2 -> 10 (2, 1) -----------------|
    3 -> 11 (2, 2)                  |
                                    |
    4 -> 100 (3, 1) ----------------|
    5 -> 101 (3, 2)                 |
    6 -> 110 (3, 2)                 |
    7 -> 111 (3, 3)                 |
                                    |
    8 -> 1000 (3, 1) _______________| 
    9 -> 1001 (3, 2)
    10 -> 1010 (3, 1)
    11 -> 1011 (3, 2)
    12 -> 1100 (3, 1)
    13 -> 1101 (3
    14 -> 1110 (4, )
    15 -> 1111 (4


    Oh, I can see a pattern:
        bits[n] = 1 + bits[n exlude most significant bits of n]
        // Look up is O(1), iterate takes O(n)
    """
    def countBits(self, n: int):

        def fn_largest_bit(num):
            # There must have bitwise op that do this
            return (int) (math.log2(num))
        def fn_remove_largest_bit(num):
            pos = fn_largest_bit(num)
            return num ^ (1 << pos)

        res = []
        for num in range(0, n + 1):
            if num == 0:
                res.append(0)
            else:
                index = fn_remove_largest_bit(num)
                res.append(1 + res[index])
        return res


if __name__ == "__main__":
    solution = Solution()

    n = 2
    res = solution.countBits(n)
    if res != [0, 1, 1]:
        raise Exception(f"Expected: {[0, 1, 1]}, got {res}")

    n = 5
    res = solution.countBits(n)
    if res != [0, 1, 1, 2, 1, 2]:
        raise Exception(f"Expected: {[0, 1, 1, 2, 1, 2]}, got {res}")
