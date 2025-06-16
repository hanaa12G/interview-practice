"""
Given two strings text1 and text2, return the length of their longest common
subsequence. If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string
with some characters (can be none) deleted without changing the relative order
of the remaining characters.

For example, "ace" is a subsequence of "abcde".

A common subsequence of two strings is a subsequence that is common to both
strings.


Example 1:

Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.

Example 2:

Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.

Example 3:

Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.



"""


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        cache = {}

        def step(a, b):
            if not a or not b:
                return 0

            a0 = a[0]
            b0 = b[0]

            key = (len(a), len(b), )
            if key in cache:
                return cache[key]


            if a0 == b0:
                res = 1 + step(a[1:], b[1:])
            else:
                res = max(step(a[1:], b), step(a, b[1:]))

            cache[key] = res

            return res

        return step(text1, text2)

if __name__ == "__main__":
    solution = Solution()

    res = solution.longestCommonSubsequence("abcde", "ace")
    if res != 3:
        raise Exception(f"\"abcde\", \"ace\". Expected 3, got {res}")

    res = solution.longestCommonSubsequence("abc", "abc")
    if res != 3:
        raise Exception(f"\"abc\", \"abc\". Expected 3, got {res}")

    res = solution.longestCommonSubsequence("abc", "def")
    if res != 0:
        raise Exception(f"\"abc\", \"def\". Expected 0, got {res}")

    res = solution.longestCommonSubsequence("bsbininm", "jmjkbkjkv")
    if res != 1:
        raise Exception(f"\"bsbininm\", \"jmjkbkjkv\". Expected 1, got {res}")

    res = solution.longestCommonSubsequence("pmjghexybyrgzczy", "hafcdqbgncrcbihkd")
    if res != 4:
        raise Exception(f"\"bsbininm\", \"jmjkbkjkv\". Expected 4, got {res}")
