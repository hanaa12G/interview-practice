"""
There is a robot on an m x n grid. The robot is initially located at the 
top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right
corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right
at any point in time.

Given the two integers m and n, return the number of possible unique paths that
the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to
2 * 109.
"""

from pprint import pprint

class Solution:
    """
    # Idea:

    On m x n grid, when robot steps down, the possible way to reach
    is equal to scenario that robot stay at initial position on m - 1 x n grid.
    Similarly, when robot steps to the right, it's like robot stays on initial
    position on m x n-1 grid

    # Fomula:
    Let's call the number of possible paths of grid m x n is P(m, n)
    1. When m = 1, then P(m, n) = m (only take right step)
    2. When n = 1, then P(m, n) = n (only take step down)
    3. When m > 1, n > 1, then P(m, n) = P(m - 1, n) + P(m, n-1) (E)
        > Why '+': because we counting possible paths, we only either take step
        to the right or a step down, so one action does not affect possible
        paths of other action
        > Is there any more operands in (E)? No, if m-2,..., m-x is already
        count in m-1, and we don't take 2 step at once
    
    # Implementation
    1. A recursive function, which check base cases (1 & 2) or recurse itself
    when it meets case 3

    2. A hash table which takes (m, n) as key and we can look up the result if
    we already calculate it before


    # Complexity:

    1. Time: O(2^(m+n)) if there isn't any caching, if there's caching I don't
    know, once we finished let's plot the runtime 
    2. Space: O(mn) to cache result of every cell in grid
    
    """
    def uniquePaths(self, m: int, n: int) -> int:

        cache = {}

        def step(a, b):

            if a == 0:
                return 1
            if b == 0:
                return 1

            key = (a, b, )
            if key in cache:
                return cache[key]
            
            count = step(a - 1, b) + step(a, b - 1)

            cache[key] = count

            return count


        res = step(m - 1, n - 1)
        return res



if __name__ == "__main__":
    solution = Solution()

    res = solution.uniquePaths(3, 2)
    assert res == 3, f"Expect 3, got {res}"

    res = solution.uniquePaths(3, 7)
    assert res == 28, f"Expect 28, got {res}"
