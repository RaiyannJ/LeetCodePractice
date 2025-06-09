class Solution(object):
    def carFleet(self, target, position, speed):

        # have the position and the time they reach the target in an array
        pairs = [(p, float(target - p) / s) for p, s in zip(position, speed)]
        pairs.sort(reverse=True)  # sort by position descending

        fleets = 0
        stack = []

        # monotonic decreasing stack
        for pos, time in pairs:
            if not stack or time > stack[-1]:
                fleets += 1
                stack.append(time)

        return fleets
