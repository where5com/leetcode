class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen=dict()
        '''
        store the seen pair (num,index)
        if seen[target-nums[i]] is already seen, then they will be the solution
        '''
        for i in range(len(nums)):
            s=target-nums[i]
            if s in seen:
                return [seen[s],i]
            seen[nums[i]]=i
    
        