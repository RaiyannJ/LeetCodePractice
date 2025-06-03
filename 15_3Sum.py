class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums) # sort for 2 pointers, O(nlgn)
        res = []
        seen = set() # track what triplets have been seen
        n = len(nums)

        for i in range(n):
            # can skip the dupe checking
            # # Skip duplicates for i, saves time
            # if i > 0 and nums[i] == nums[i - 1]:
            #     continue

            target = -nums[i] # goal is nums[l] + nums[r] = -nums[i]
            l= i + 1 # beautiful algorithm, l will always just be the first one to the right of i
            r = n - 1

            # now we do 2 pointer for each target (each nums[i]), so O(n^2)

            # 2 pointer conditions
            while l < r:
                curr_sum = nums[l] + nums[r]

                # normal 2 pointer
                if curr_sum < target:
                    l += 1
                elif curr_sum > target:
                    r -= 1
                else:
                    # check no duplicate truples
                    triplet = (nums[i], nums[l], nums[r])
                    if triplet not in seen:
                        res.append(list(triplet))
                        seen.add(triplet)
                    l += 1
                    r -= 1
                    
                    # can skip dupe checking
                    # # Skip duplicates for l and r
                    # while l < r and nums[l] == nums[l - 1]:
                    #     l += 1
                    # while l < r and nums[r] == nums[r + 1]:
                    #     r -= 1

        return res
