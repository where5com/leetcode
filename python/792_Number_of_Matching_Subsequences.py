class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        count=0
        for ss,times in Counter(words).items():
            '''
            ss words in the list "words"
            times:num of duplicates of ss in "words"

            '''
            start=-1
            for c in ss:
                if not (start:=(s.find(c,start+1)))>=0:                   
                    break
            else:
                count+=times

        return count
        