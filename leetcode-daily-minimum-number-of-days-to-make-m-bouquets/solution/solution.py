from typing import List

class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        def isValid(x):
            total, currcount = 0, 0
            for b in bloomDay:
                if b <= x:
                    currcount += 1
                else:
                    total += currcount // k
                    if total >= m:
                        return True
                    currcount = 0
            return total + currcount // k >= m

        if m*k > len(bloomDay):
            return -1
        left, right = min(bloomDay), max(bloomDay)
        while left < right:
            mid = left + (right - left)//2
            if isValid(mid):
                right = mid
            else:
                left = mid + 1
        return left