"""
Given an array of intervals intervals where intervals[i] = [starti, endi], return
the minimum number of intervals you need to remove to make the rest of the
intervals non-overlapping.

Note that intervals which only touch at a point are non-overlapping. For example,
[1, 2] and [2, 3] are non-overlapping.



Example 1:

Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of the intervals are 
non-overlapping.

Example 2:

Input: intervals = [[1,2],[1,2],[1,2]]
Output: 2
Explanation: You need to remove two [1,2] to make the rest of the intervals 
non-overlapping.

Example 3:

Input: intervals = [[1,2],[2,3]]
Output: 0
Explanation: You don't need to remove any of the intervals since they're already
non-overlapping.



Constraints:

    1 <= intervals.length <= 105
    intervals[i].length == 2
    -5 * 104 <= starti < endi <= 5 * 104
"""

from typing import List
from functools import cmp_to_key

class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end   = end

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        def compare_interval(a, b):
            if a[0] != b[0]:
                return a[0] - b[0]
            else:
                return a[1] - b[1]

        intervals = sorted(intervals, key=cmp_to_key(compare_interval))
        interval_map = dict()
        for interval in intervals:
            interval_map.setdefault(interval[0], []).append(interval[1])

        count = 0
        last_key = None
        for key, vs in interval_map.items():
            if last_key:
                if key < interval_map[last_key][0]:
                    count += len(vs)
            else:
                last_key = key
                count += len(vs) - 1
                interval_map[key] = vs[:1]
        return count

if __name__ == "__main__":
    solution = Solution()

    res = solution.eraseOverlapIntervals([[1, 2], [2, 3], [3, 4], [1, 3]])
    expect = 1
    if res != expect:
        raise Exception(f"Test case 1, expect {expect} != res {res}")

    res = solution.eraseOverlapIntervals([[1, 2], [1, 2], [1, 2]])
    expect = 2
    if res != expect:
        raise Exception(f"Test case 2, expect {expect} != res {res}")

    res = solution.eraseOverlapIntervals([[1, 2], [2, 3]])
    expect = 0
    if res != expect:
        raise Exception(f"Test case 3, expect {expect} != res {res}")
