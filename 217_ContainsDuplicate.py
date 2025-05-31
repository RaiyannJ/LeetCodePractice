class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        mySet = set()

        # simple, hashsets don't contain duplicate
        for e in nums:
            if e in mySet:
                return True
            else:
                mySet.add(e)

        return False
        