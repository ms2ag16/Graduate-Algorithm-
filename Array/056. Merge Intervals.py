"""
Given a collection of intervals, merge all overlapping intervals.

Example 1:
Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
"""
# Definition for an interval.
class Interval(object):
     def __init__(self, s=0, e=0):
         self.start = s
         self.end = e
     def __str__(self):
         return "[" + str(self.start) +","+str(self.end)+"]"

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if not intervals:
            return []
        intervals.sort(key=lambda x:x.start)
        tail=0
        for interval in intervals:
            if interval.start>intervals[tail].end:
                tail+=1
                intervals[tail]=interval
            else:
                intervals[tail].end=max(intervals[tail].end, interval.end)
        return intervals[:tail+1]
         
        

    
if __name__ == "__main__":
    intervals = Solution().merge([Interval(1, 3), Interval(2, 6), Interval(8, 10), Interval(15, 18)])
    for interval in intervals:
        print(interval)
        
        
