class Solution:
    def minCut(self, s: str) -> int:
        # dynamic programming with indexed of index of last character.
        # dp[m] (or opt[m])  is the minimum num of cuts so that s[:m+1] can 
        # be partitioned into palindrome strings.
        # the otp[m]=0 if s[0:m+1] is a palindrome string;
        # otherwise there exists last cut from range(1,m),
        # in this case opt[m]=min(dp[0],...,dp[m-1])+1.
        
        import numpy as np
        n=len(s)
        
        isP=np.full((n,n),1)
        # isP[i][j] determine whther s[i:j+1] is a palindrome string
        for i in range(n-1):
            if s[i]!=s[i+1]:
                isP[i][i+1]=0
                
        for gap in range(2,n):
            for i in range(n-gap):
                if not(s[i]==s[i+gap] and isP[i+1][i+gap-1]):
                    isP[i][i+gap]=0 
      
        # dynamic programming with preceding optimal substructure
        dp=np.zeros((n),dtype='int')
        for j in range(1,n):
            if isP[0][j]==1:
                continue
            dp[j]=dp[j-1]+1
            for i in range(1,j):
                if isP[i][j]:
                    dp[j]=min(dp[j],dp[i-1]+1)
                
        return dp[n-1]