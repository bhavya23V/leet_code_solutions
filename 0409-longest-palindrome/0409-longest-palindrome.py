class Solution:
    def longestPalindrome(self, s: str) -> int:
        ans = 0
        odd = 0

        for c in set(s):
            n = s.count(c)
            ans += n - n % 2
            if n % 2:
                odd = 1

        return ans + odd