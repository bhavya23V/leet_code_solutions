class Solution:
    def xorAfterQueries(self, nums, queries):
        MOD = 10**9 + 7
        for l, r, k, v in queries:
            idx = l
            while idx <= r:
                nums[idx] = (nums[idx] * v) % MOD
                idx += k
        answer = 0
        for num in nums:
            answer ^= num
        return answer