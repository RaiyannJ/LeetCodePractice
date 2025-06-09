class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """

        # monotonic decreasing stack
        stack = []

        res = [0] * len(temperatures)

        # O(n)
        for i in range(len(temperatures)):

            # While the stack is not empty and the current temperature is greater
            # than the temperature at the index on the top of the stack,
            # it means we've found the next warmer day for that index
            while stack and temperatures[i] > temperatures[stack[-1]]:
                index = stack.pop()
                res[index] = i - index 
            stack.append(i)
        return res