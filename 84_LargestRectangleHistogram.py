class Solution(object):
    def largestRectangleArea(self, heights):
        n = len(heights)
        maxArea = 0
        stack = []

        # iterate through each bar (and one extra step to flush the stack at the end)
        for i in range(n + 1):
            # hile the stack is not empty and the current bar is shorter than the top of the stack
            # this means we've found a boundary for the rectangle with the height of the popped bar
            while stack and (i == n or heights[stack[-1]] >= heights[i]):
                # op the index of the height to compute area
                height = heights[stack.pop()]
                
                # alculate the width:
                # if stack is empty, it means the popped bar is the smallest so far, so width is i
                # else, width is between current index and new top of stack
                width = i if not stack else i - stack[-1] - 1
                
                maxArea = max(maxArea, height * width)
            
            # push the current index onto the stack
            stack.append(i)
        
        return maxArea
