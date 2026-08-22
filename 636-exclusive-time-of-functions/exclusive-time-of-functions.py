class Solution(object):
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        res = [0] * n
        stack = []
        prev_time = 0
        
        for log in logs:
            fn_id, action, timestamp = log.split(":")
            fn_id = int(fn_id)
            curr_time = int(timestamp)
            if action=="start":
                if stack:
                    res[stack[-1]]+= curr_time -prev_time
                stack.append(fn_id)
                prev_time = curr_time
            else: 
                res[stack.pop()] += curr_time -prev_time+ 1
                prev_time =curr_time + 1       
        return res