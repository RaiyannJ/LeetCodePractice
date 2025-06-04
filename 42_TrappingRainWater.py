class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        l = 0
        r = len(height) - 1

        res = 0

        # init 2 maxes
        leftmax = height[l]
        rightmax = height[r]

        # 2 pointer condition
        while l < r:

            #move the pointer that has the smaller max first
            if leftmax < rightmax:
                l+=1
                # see if new max
                leftmax = max(leftmax, height[l])
                # area will be this difference accumulated
                res += leftmax - height[l]

            # same thing on right side
            elif rightmax <= leftmax:
                r-=1
                rightmax = max(rightmax, height[r])
                res += rightmax - height[r]
        return res