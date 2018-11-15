# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        if not intervals:
            return 0
        free_rooms=[]
        intervals.sort(key=lambda x: x.start)
        import heapq
        heapq.heappush(free_rooms, intervals[0].end)
        for i in intervals[1:]:
            if free_rooms[0]<=i.start:
                heapq.heappop(free_rooms)
            heapq.heappush(free_rooms, i.end)
        return len(free_rooms)
