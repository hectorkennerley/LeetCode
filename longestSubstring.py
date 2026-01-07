class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLen = 0
        lPointer = 0
        rPointer = 0
        while lPointer < len(s):
            while rPointer <= len(s):
                if len(set(s[lPointer:rPointer])) == len(s[lPointer:rPointer]):
                    maxLen = max(maxLen, len(s[lPointer:rPointer]))
                    rPointer += 1
                else:
                    lPointer += 1
                    rPointer = lPointer
            lPointer += 1
            rPointer = lPointer
        return maxLen
