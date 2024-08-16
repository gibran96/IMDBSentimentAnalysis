from typing import List


def insert(intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                result.append(newInterval)
                return result + intervals[i:]
            elif newInterval[0] > intervals[i][1]:
                result.append(intervals[i])
            else:
                newInterval[0] = min(newInterval[0], intervals[i][0])
                newInterval[1] = max(newInterval[1], intervals[i][1])

        result.append(newInterval)
        return result

# print(insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8])) # [[1,5],[6,9]]

def merge(intervals: List[List[int]]) -> List[List[int]]:
    res = []
    intervals.sort(key=lambda x: x[0])
    for i in intervals:
        if not res or res[-1][1] < i[0]:
            res.append(i)
        else:
            res[-1][1] = max(res[-1][1], i[1])
    return res

# print(merge([[1,3],[2,6],[8,10],[15,18]])) # [[1,6],[8,10],[15,18]]

def eraseOverlapIntervals(intervals: List[List[int]]) -> int:
    res = 0
    intervals.sort()
    prevEnd = intervals[0][1]

    for start, end in intervals[1:]:
        if prevEnd <= start:
            prevEnd = end
        else:
            res += 1
            prevEnd = min(end, prevEnd)
    return res


# print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]))

class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

def canAttendMeetings(intervals: List[Interval]) -> bool:
    if not intervals:
        return True
    
    intervals.sort(key=lambda x: x.start)
    
    prevEnd = intervals[0].end

    for interval in intervals[1:]:
        start, end = interval.start, interval.end
        if start < prevEnd:
            return False
        else:
            prevEnd = end
    
    return True

# print(canAttendMeetings([]))

def minMeetingRooms(intervals: List[Interval]) -> int:
    res = 0
    intervals.sort(key=lambda x: x.start)
    prevEnd = intervals[0].end

    for interval in intervals[1:]:
        start, end = interval.start, interval.end
        if prevEnd <= start:
            prevEnd = end
        else:
            res += 1
            prevEnd = max(end, prevEnd)
    return res

i1 = Interval(0,40)
i2 = Interval(5,10)
i3 = Interval(15,20)

# print(minMeetingRooms([i1, i2, i3]))

def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
    l, r = 0, len(matrix[0])
    top, bottom = 0, len(matrix)
    res = []
    while l < r and top < bottom:
        for i in range(l, r):
            res.append(matrix[top][i])
        top += 1

        for i in range(top, bottom):
            res.append(matrix[i][r - 1])
        r -= 1

        if not (l < r or top < bottom): break

        for i in range(r - 1, l - 1, -1):
            res.append(matrix[bottom - 1][i])
        bottom -= 1

        for i in range(bottom - 1, top - 1, -1):
            res.append(matrix[i][l])
        
        l += 1
    
    return res


def checkInclusion(s1: str, s2: str) -> bool:
        s1_map = {}
        for c in s1:
            s1_map[c] = 1 + s1_map.get(c, 0)
        print(s1_map)
        
        l, r = 0, len(s1) - 1

        while r <= len(s2) - 1:
            temp = s2[l:r + 1]
            temp_map = {}
            for c in temp:
                temp_map[c] = 1 + temp_map.get(c, 0)
            if temp_map == s1_map:
                return True
            l += 1
            r += 1
        
        return False


# print(checkInclusion("adc", "dcda"))

def minEatingSpeed(piles: List[int], h: int) -> int:
    minK = 99999999999999
    l, r = 1, max(piles)
    while l < r:
        k = (l + r) // 2
        resH = 0
        for n in piles:
            resH += (n // k) + (n % k > 0)
        if resH <= h:
            minK = min(minK, k)
            r = k - 1
        else:
            l = k + 1
        
    return minK

print(minEatingSpeed([30,11,23,4,20], 5))