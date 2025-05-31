class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        map = {}

        # search for target - nums[i] in set
        for i in range(len(nums)):
            res = target - nums[i]
            if res not in map:
                map[nums[i]] = i
            else:
                return(i, map[res])