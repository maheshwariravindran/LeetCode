class Solution(object):
    def shuffle(self, nums, n):
        res = []
        for x, y in zip(nums[:n], nums[n:]):
            res.append(x)
            res.append(y)
        return res