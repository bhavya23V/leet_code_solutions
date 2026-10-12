class Solution:
    def longestNiceSubstring(self, s):
        if len(s) < 2:
            return ""

        char_set = set(s)

        for i in range(len(s)):
            if s[i].lower() in char_set and s[i].upper() in char_set:
                continue

            left = self.longestNiceSubstring(s[:i])
            right = self.longestNiceSubstring(s[i + 1:])

            if len(left) >= len(right):
                return left
            else:
                return right

        return s