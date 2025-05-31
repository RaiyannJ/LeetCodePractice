class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        # init pointers
        l = 0
        r = len(numbers) - 1

        #iterate until converge or target
        while l < r:
            if (numbers[l] + numbers[r]) > target:
                r -=1
            elif (numbers[l] + numbers[r]) < target:
                l +=1
            elif (numbers[l] + numbers[r]) == target:
                return [l+1, r+1] # wanted 1-indexed