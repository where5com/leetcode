class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char={}
        start=0
        maxlen=0
        for i,c in enumerate(list(s)):
            if c in char:
                start=max(char[c]+1,start)
            char[c]=i
            maxlen=max(maxlen,i-start+1)
        return maxlen