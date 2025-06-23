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
        If we have N numbers we should have N/2 distinct values. Creating N/2
        element arrays is not linear

        We can move element around, the there's no way to know if a duplicate
        exist.

        Why the length constraint the number value constraint need to be so
        similar?

        Array length is always 2N + 1, so if length is 5, we can have values
        like:
            * [1, 1, 2, 2, 0]
            * [-3 * 104, -3 * 104, 5, 5, 102]

        But if N is not so large why the need for constant space, 3 * 104
        element is not large

        We can event reduce that by setting each bit, 1 byte = 8 bit,
        3 * 104 / 2 =  156 bit = 19.5 bytes

        Create an array of 20 bytes is enough, constant space !!

    """
    def singleNumber(self, nums: List[int]) -> int:
        # print(f'Single Number: { nums }')
        checklist = [0] * 10000

        for num in nums:
            num += 3 * pow(10, 4)
            num_bytes = math.floor(num / 8)
            num_bits  = num % 8

            # print(f'num={num}, bytes={num_bytes}, bits={num_bits}')

            cell = checklist[num_bytes]
            # print('cell before: {0:08b}'.format(cell))
            has_set = cell & ( 1 << num_bits)

            if has_set:
                cell = cell & (0xff ^ (1 << num_bits))
            else:
                cell = cell | (1 << num_bits)
            # print('cell after: {0:08b}'.format(cell))
            checklist[num_bytes] = cell

        ss = ""
        the = None
        for i in range(0, len(checklist)):
            ss += "{0:08b}".format(checklist[i])
            for j in range(0, 8):
                has_set = checklist[i] & (1 << j)
                if has_set:
                    # print(f"Found i={i}, j={j}")
                    the = i * 8 + j
                    break
            if the:
                break
            ss += " "
        # print(ss)
        the -= 3 * pow(10, 4)
        return the



if __name__ == "__main__":

    solution = Solution()


    # res = solution.singleNumber([2, 2, 1])
    # if res != 1:
    #     raise Exception(f"Expect {1}, got {res}")

    # res = solution.singleNumber([4, 1, 2, 1, 2])
    # if res != 4:
    #     raise Exception(f"Expect {4}, got {res}")

    # res = solution.singleNumber([1])
    # if res != 1:
    #     raise Exception(f"Expect {1}, got {res}")
    # res = solution.singleNumber([-1])
    # if res != -1:
    #     raise Exception(f"Expect {-1}, got {res}")
    res = solution.singleNumber([-80,48,777,423,-435,349,-988,-379,-197,192,13,-496,-787,94,329,-490,-230,-929,457,591,75,-80,48,777,423,-435,349,-988,-379,-197,192,13,-496,-787,94,329,-490,-230,-929,457,591,75,-477])
    if res != -477:
        raise Exception(f"Expect {-477}, got {res}")
