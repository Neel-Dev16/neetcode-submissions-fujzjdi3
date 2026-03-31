"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if len(intervals)<1:
            return True
        intervals.sort(key=lambda x:x.start)
        initial=intervals[0].end
        for i in intervals[1:]:
            if i.start<initial:
                return False
            initial=i.end
        return True

