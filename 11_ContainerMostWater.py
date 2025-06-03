class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # 2 pointer setup
        l = 0
        r = len(height) - 1

        res = 0

        # 2 pointer while loop
        while l < r:
            # height will be smaller of 2 ends
            h = min(height[l], height[r])
            # calculate area
            temp = h * (r - l)
            # store highest area so far
            res = max(res, temp)
            
            # greedy approach, want to make the shorter side taller
            if height[l] < height[r]:
                l +=1
            else:
                r -=1
        
        return res