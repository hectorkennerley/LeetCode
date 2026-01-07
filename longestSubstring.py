class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        for i in range(0,len(s)):
            for j in range(0,len(s)):
                if len(set(s[i:j])) == len(s[i:j]) and len(s[i:j]) > max_len:
                    max_len = len(s[i:j])
        return max_len
