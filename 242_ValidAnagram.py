class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        if len(s) != len(t):
            return False
        
        freqS = {}
        freqT = {}

        for i in range(len(s)):
            freqS[s[i]] = freqS.get(s[i], 0) +1
            freqT[t[i]] = freqT.get(t[i], 0) +1
        
        for c in freqS:
            if freqS[c] != freqT.get(c,0):
                return False
        
        return True