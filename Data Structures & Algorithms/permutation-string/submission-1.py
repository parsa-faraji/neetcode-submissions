from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # we want to check if some combination of letters on s1 exists
        # in s2. The window we're looking for is of size len(s1)
        # we can start by having a window of that size move from left to right in 
        # s2, and checking if it has all the letters in s1 with the right count.

        size = len(s1)
        if size > len(s2):
            return False

        target = Counter(s1)
        window = Counter(s2[:size])
        if window == target:
            return True

        for right in range(size, len(s2)):
            window[s2[right]] += 1
            left_Char = s2[right - size]
            window[left_Char] -= 1
            if window[left_Char] == 0:
                del window[left_Char]
            if window == target:
                return True
        return False

