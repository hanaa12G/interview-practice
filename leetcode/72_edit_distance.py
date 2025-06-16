"""
Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

You have the following three operations permitted on a word:

    Insert a character
    Delete a character
    Replace a character

 

Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')

Example 2:

Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation: 
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')

 

Constraints:

    0 <= word1.length, word2.length <= 500
    word1 and word2 consist of lowercase English letters.


"""


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        tab = []
        cache = {}

        def step(i, j):
            tab.append('_')
            prefix = ''.join(tab)
            if j >= len(word2):
                #print(f'{prefix}<- Return')
                tab.pop()
                cache[(i, j, )] = len(word1) - i
                return len(word1) - i
            elif i >= len(word1):
                #print(f'{prefix}<- Return')
                tab.pop()
                cache[(i, j, )] = len(word2) - j
                return len(word2) - j

            #print(f'{prefix}{word1[0: i]}[{word1[i]}]{word1[i + 1:]}')
            #print(f'{prefix}{word2[0: j]}[{word2[j]}]{word2[j + 1:]}')

            if (i, j, ) in cache:
                return cache[(i, j, )]

            rem1 = len(word1) - i
            rem2 = len(word2) - j

            if word1[i] == word2[j]:
                #print(f'{prefix}..Case 0')
                res = step(i + 1, j + 1)
            else:
                #print(f'{prefix}..Case 1_1')
                res1 = step(i + 1, j + 1)

                #print(f'{prefix}..Case 1_2')
                res2 = step(i + 1, j)

                #print(f'{prefix}..Case 1_3')
                res3 = step(i, j + 1)

                res = 1 + min(res1, res2, res3)

            # elif rem1 > rem2:
            #     #print(f'{prefix}..Case 1_1')
            #     res1 = step(i + 1, j + 1)
            #     #print(f'{prefix}..Case 1_2')
            #     res2 = step(i + 1, j)
            #     res = 1 + min(res1, res2)
            # elif rem1 < rem2:
            #     #print(f'{prefix}..Case 2_1')
            #     res1 = step(i + 1, j + 1)

            #     #print(f'{prefix}..Case 2_2')
            #     res2 = step(i, j + 1)

            #     res = 1 + min(res1, res2)
            # else:
            #     #print(f'{prefix}..Case 3_1')
            #     res1 = step(i + 1, j + 1)

            #     #print(f'{prefix}..Case 3_2')
            #     res2 = step(i, j + 1)

            #     #print(f'{prefix}..Case 3_3')
            #     res3 = step(i + 1, j)

            #     res = 1 + min(res1, res2, res3)
            tab.pop()
            cache[(i, j, )] = res
            return res


        return step(0, 0)

if __name__ == "__main__":

    solution = Solution()

    res = solution.minDistance("horse", "ros")
    if res != 3:
        raise Exception(f"Expect {3}, got {res}")

    res = solution.minDistance("intention", "execution")
    if res != 5:
        raise Exception(f"Expect {5}, got {res}")

    res = solution.minDistance("b", "")
    if res != 1:
        raise Exception(f"Expect {1}, got {res}")

    res = solution.minDistance("sea", "eat")
    if res != 2:
        raise Exception(f"Expect {2}, got {res}")

    res = solution.minDistance("trinitrophenylmethylnitramine", "dinitrophenylhydrazine")
    if res != 10:
        raise Exception(f"Expect {10}, got {res}")

    res = solution.minDistance("teacher", "tenace")
    if res != 3:
        raise Exception(f"Expect {3}, got {res}")
