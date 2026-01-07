class Solution:
    def longestPalindrome(self, s: str) -> str:
        s = self.addat(s)
        longest = ""
        for i in range(0, len(s)):
            w = 0
            isPalindrome = True
            while i - w >= 0 and i + w < len(s) and isPalindrome:
                if s[i-w] == s[i+w]:
                    if 2*w+1 > len(longest):
                        longest = s[i - w:i + w + 1]
                else:
                    isPalindrome = False
                w += 1
        return self.removeat(longest)


    def addat(self, s):
        if s == '':
            return ["@"]
        return ["@",s[0]] + self.addat(s[1:])


    def removeat(self, s):
        if s == []:
            return ''
        if s[0] == "@":
            return self.removeat(s[1:])
        return s[0] + self.removeat(s[1:])
