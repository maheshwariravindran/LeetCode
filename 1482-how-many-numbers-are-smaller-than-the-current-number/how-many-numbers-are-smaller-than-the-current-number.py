class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        count = []
        for i in nums:
            lcount = 0  
            for j in nums:
                if i > j:
                    lcount += 1
            count.append(lcount) 
        return count