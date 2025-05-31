class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        # Count the number of zeros in nums
        zero_count = nums.count(0)

        # If more than one zero, all products except self will be 0
        if zero_count > 1:
            return [0] * len(nums)

        # If exactly one zero, only one position will be non-zero
        if zero_count == 1:
            prod = 1
            zero_index = -1
            for i, num in enumerate(nums):
                if num != 0:
                    prod *= num
                else:
                    zero_index = i
            res = [0] * len(nums)
            res[zero_index] = prod
            return res

        # No zeros, proceed with normal logic
        res = [0] * len(nums)
        res[0] = nums[0]
        for i in range(1, len(nums)):
            res[i] = res[i-1] * nums[i]

        prod = res[len(nums)-1]
        res = [prod / e for e in nums]
        return res