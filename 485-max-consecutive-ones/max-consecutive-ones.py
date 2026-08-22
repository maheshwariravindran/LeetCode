class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = []
        lcount = 0
        for i in nums:
            
            if i==1:
                lcount+=1
            elif i==0:
                lcount = 0
           
            count.append(lcount)
        return max(count)



        