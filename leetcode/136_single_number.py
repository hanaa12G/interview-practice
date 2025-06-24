"""
Given a non-empty array of integers nums, every element appears twice except 
for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only 
constant extra space.

 

Example 1:

Input: nums = [2,2,1]

Output: 1

Example 2:

Input: nums = [4,1,2,1,2]

Output: 4

Example 3:

Input: nums = [1]

Output: 1

 

Constraints:

    1 <= nums.length <= 3 * 10^4
    -3 * 10^4 <= nums[i] <= 3 * 10^4
    Each element in the array appears twice except for one element which appears only once.


"""

import math
from typing import List

class Solution:
    """
        Same idea as previous attemp, I notice that xor operaton has associative
        property
        [link](https://en.wikipedia.org/wiki/Bitwise_operation#Boolean_algebra)

        Because of that, we have 3 following equation
        
        x ^ y ^ z = (x ^ y) ^ z = x ^ (y ^ z) -> P1

        x ^ x = 0 -> P2

        x ^ 0 = x -> P3


        We can have a single integer, xor each number and the final result is
        out single number.

        x ^ y ^ z ^ x ^ z = (x ^ x) ^ (z ^ z) ^ y = 0 ^ 0 ^ y = y
            ....... P1....... P2..........................P3.....


    """
    def singleNumber(self, nums: List[int]) -> int:
        res = 0

        for num in nums:
            res = res ^ num
        return res



if __name__ == "__main__":

    solution = Solution()


    res = solution.singleNumber([2, 2, 1])
    if res != 1:
        raise Exception(f"Expect {1}, got {res}")

    res = solution.singleNumber([4, 1, 2, 1, 2])
    if res != 4:
        raise Exception(f"Expect {4}, got {res}")

    res = solution.singleNumber([1])
    if res != 1:
        raise Exception(f"Expect {1}, got {res}")
    res = solution.singleNumber([-1])
    if res != -1:
        raise Exception(f"Expect {-1}, got {res}")
    res = solution.singleNumber([-80,48,777,423,-435,349,-988,-379,-197,192,13,-496,-787,94,329,-490,-230,-929,457,591,75,-80,48,777,423,-435,349,-988,-379,-197,192,13,-496,-787,94,329,-490,-230,-929,457,591,75,-477])
    if res != -477:
        raise Exception(f"Expect {-477}, got {res}")
