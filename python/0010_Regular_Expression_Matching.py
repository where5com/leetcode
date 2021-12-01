#Dynamic Programming for Expression Matching
'''
1.dp[i][j] descripte that whether s[:i] and p[:j] are matching
2-1.Initional matching for "" and p[:i], i from 0 to len(p)
2-2.OTP[i][j]=OTP1[i][j] || OTP2[i][j] ||OTP3[i][j] 
    where
    OTP1[i][j]= matching through aline s[i-1] and p[j-1]
    OTP2[i][j]= matching through repeat p[j-2] 1 or more than 1-times 
    OTP3[i][j]= matching s[:i] and p[:j-2]
3.return dp[m][n], m=len(s), n=len(p) 
'''

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m=len(s)+1
        n=len(p)+1
        import numpy as np
        dp=np.zeros((m,n),dtype=bool)
        ########initial condition########
        dp[0][0]=True
        if s[0]==p[0] or p[0]=='.': dp[1][1]=True
        for j in range(2,n):
            if p[j-1]=='*' and dp[0][j-2]:
                dp[0][j]=True
        ################################# 
        
        for i in range(1,m):
            for j in range(2,n):
                if (s[i-1]==p[j-1] or p[j-1]=='.') and dp[i-1][j-1]:
                    dp[i][j]=True
                elif p[j-1]=='*':
                    if (s[i-1]==p[j-2] or p[j-2]=='.') and (dp[i-1][j-1] or dp[i-1][j]):
                        dp[i][j]=True
                    elif dp[i][j-1] or dp[i][j-2]:
                        dp[i][j]=True
        return dp[m-1][n-1]
        