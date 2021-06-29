class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        '''
        que:record the 0-bit who fliped to 1
        start: current start position of consecutive 1s
        if nums[i]==1 record the position i by append in the que,
        if there are k-positions already in que, remove the right-most 1, and then append the newest i
        the longest consecutive 1s sequence is the one of [start,i]
        update the maxlen in each run of for-loop
        '''
        que=[]
        maxlen=0
        start=0
        for i in range(len(nums)):
            if nums[i]==0:
                if len(que)<k:
                    que.append(i)
                elif k>0:
                    start=que.pop(0)+1
                    que.append(i)
                else:
                    start=i+1
            maxlen=max(maxlen,i-start+1)
                      
        return maxlen