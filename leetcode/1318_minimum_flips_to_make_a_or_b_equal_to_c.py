"""
Given 3 positives numbers a, b and c. Return the minimum flips required in some
bits of a and b to make ( a OR b == c ). (bitwise OR operation).

Flip operation consists of change any single bit 1 to 0 or change the bit 0 to 
1 in their binary representation.

Example 1:

Input: a = 2, b = 6, c = 5
Output: 3
Explanation: After flips a = 1 , b = 4 , c = 5 such that (a OR b == c)

Example 2:

Input: a = 4, b = 2, c = 7
Output: 1

Example 3:

Input: a = 1, b = 2, c = 3
Output: 0

 

Constraints:

    1 <= a <= 10^9
    1 <= b <= 10^9
    1 <= c <= 10^9

"""


class Solution:
    """
    At bit N.
        a[N] = 1
        b[N] = 1
        c[N] = 0

    This case only need 2 flips to make, otherwise we need only 1 or 0 flip
    
    """
    def minFlips(self, a: int, b: int, c: int) -> int:

        rem = c ^ (a | b)
        flips = 0

        while rem != 0:
            lastbit = rem & 1
            lastbit_a = a & 1
            lastbit_b = b & 1
            lastbit_c = c & 1
            
            # print('a = {:08b}, b = {:08b}, c = {:08b}'.format(a, b, c))
            # print('rem={:08b}'.format(rem))

            if lastbit == 1:
                # Here we need to check

                if (lastbit_a == 1 and lastbit_b == 1 and lastbit_c == 0):
                    # print("Add 2")
                    flips += 2
                else:
                    # print("Add 1")
                    flips += 1

            rem = rem >> 1
            a = a >> 1
            b = b >> 1
            c = c >> 1
        return flips

if __name__ == "__main__":
    solution = Solution()

    res = solution.minFlips(2, 6, 5)
    if res != 3:
        raise Exception(f"a=2, b=6, c=5. Expected 3, got {res}")

    res = solution.minFlips(4, 2, 7)
    if res != 1:
        raise Exception(f"a=4, b=2, c=7. Expected 1, got {res}")

    res = solution.minFlips(1, 2, 3)
    if res != 0:
        raise Exception(f"a=1, b=2, c=3. Expected 0, got {res}")
