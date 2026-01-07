class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # First I want a function that generates the list
        if numRows == 1:
            return s
        l = self.generateList(numRows - 1, True, len(s), 0)
        final = ""
        for i in range(0, numRows):
            for j in range(0, len(s)):
                if l[j] == i:
                    final += s[j]
        return final

    def generateList(self, n, increasing, l, i):
        if l == 0:
            return []
        if i == n:
            return [i] + self.generateList(n, False, l - 1, i - 1)
        if i == 0:
            return [i] + self.generateList(n, True, l - 1, i + 1)
        if increasing:
            return [i] + self.generateList(n, True, l - 1, i + 1)
        else:
            return [i] + self.generateList(n, False, l - 1, i - 1)
