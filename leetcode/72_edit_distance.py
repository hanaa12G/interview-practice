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
    """
    # Idea
    
    Using the same idea as last attemp, minimal distance between a
    string A[ax...am] and  B[bx...bn], suppose that we have edited the previous
    part A[a1...ax] and B[b1...bx] to be the same.

    ```
        Distance(A[ax, am], B[bx, bn]) = (int) (A[ax] == B[bx]) + min(
            Distance(A[x+1, m], B[x+1, n]), // Replace
            Distance(A[x+1, m], B[x, n]), // remove A[x] from A
            Distance(A[x, m], B[x+1, n]) // insert B[x] to A
        )
    ```

    Above idea can't not pass all test cases, because when A[x] == B[x] we
    should consider A[x+1:] B[x+1:] immediately



    Instead of using a map to store the subproblem like previous attemp, we can
    create a dynamic table (notice the pattern (x, y), (x + 1, y), (x, y+1), (x
    + 1, y+1), does this look like a table to you)

    # Example

    ## The table #1
                        h o r s e "" <- empty string
                    r              3 <- take 3 steps to convert "" to "ros"
                    o              2 <- take 2 steps to convert "" to "os"
                    s          [1] 1 <- take 1 step to convert "" to "s"
-> empty string    ""   5 4 2 2 1  0 <- take 0 step to convert "" to ""
                        | | | | |-<- take 1 step to convert "e" to ""
                        | | | |-<- "se" to "" 
                        .....

    Notice the [1] in dynamic table, because "s" is different from "e", we need
    1 + the min of right or bottom or bottom right cell. In this case we select
    bottom-right cell.

    So the transformation order:
    1. Replace "e" to "s"
    2. Replace "" to ""

    ## The table #2
                        h o r s e ""
                    r              3
                    o              2
                    s        [1]1  1
                   ""   5 4 2 2 1  0
    Transformation order from "se" to "s":
    1. As "s" is the same, we can select 1 of these 2
        1. "e" to "s" = 1, a replace
        2. "e" to "", 1, a delete
    """
    def minDistance(self, word1: str, word2: str) -> int:

        # Initialize table
        table = []

        for ri in range(0, len(word2) + 1):
            row = []
            for ci in range(0, len(word1) + 1):
                if ci != len(word1):
                    if ri != len(word2):
                        row.append(None)
                    else:
                        row.append(len(word1) - ci)
                else:
                    row.append(len(word2) - ri)
            table.append(row)


        def print_table(table):
            s = ''
            for c in word1:
                s += '{0: <4}'.format(c) + ','
            s += '\n'
            i = 0
            for row in table:
                for cell in row:
                    s +=  '{0: <4}'.format(str(cell)) + ','
                if i < len(word2):
                    s += word2[i]
                else:
                    s += 'Nan'
                s += '\n'
                i += 1
            s += '--------------------\n'
            print(s)
        # print_table(table)

        for ri in range(len(word2) - 1, -1, -1):
            for ci in range(len(word1) - 1, -1, -1):
                if word1[ci] == word2[ri]:
                    table[ri][ci] = table[ri + 1][ci + 1]
                else:
                    table[ri][ci] = 1 + min(table[ri][ci + 1], table[ri +
                                                                     1][ci],
                                            table[ri + 1][ci + 1])


                # print_table(table)
            


        return table[0][0]

if __name__ == "__main__":

    solution = Solution()

    # res = solution.minDistance("horse", "ros")
    # if res != 3:
    #     raise Exception(f"Expect {3}, got {res}")

    # res = solution.minDistance("intention", "execution")
    # if res != 5:
    #     raise Exception(f"Expect {5}, got {res}")

    # res = solution.minDistance("b", "")
    # if res != 1:
    #     raise Exception(f"Expect {1}, got {res}")

    # res = solution.minDistance("sea", "eat")
    # if res != 2:
    #     raise Exception(f"Expect {2}, got {res}")

    # res = solution.minDistance("trinitrophenylmethylnitramine", "dinitrophenylhydrazine")
    # if res != 10:
    #     raise Exception(f"Expect {10}, got {res}")

    # res = solution.minDistance("teacher", "tenace")
    # if res != 3:
    #     raise Exception(f"Expect {3}, got {res}")

    # res = solution.minDistance("zoologicoarchaeologist", "zoogeologist")
    # if res != 10:
    #     raise Exception(f"Expect {10}, got {res}")

    res = solution.minDistance("zooeolo", "zogeolo")
    if res != 1:
        raise Exception(f"Expect {1}, got {res}")
