class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = ''.join(c.lower() for c in s if c.isalnum()) # convert string to lowercase alpha num
        
        # init pointers
        l = 0
        r = len(s)-1

        # iterate until converge or terminal condition
        while l < r:
            if s[l] != s[r]:
                return False
            l+=1
            r-=1
        return True