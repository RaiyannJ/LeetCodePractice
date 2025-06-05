class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []

        # iterate through tokens
        for t in tokens:
            #check different cases
            if t == '+':
                #since polish, 2 most recently added to stack (top of stack)
                #are the ones in focus with the operand
                a = stack.pop()
                b = stack.pop()
                res = int(a) + int(b)

                # stick it back on top the stack
                stack.append(res)
            elif t == '-':
                a = stack.pop()
                b = stack.pop()
                res = int(b) - int(a)
                stack.append(res)
            elif t == '*':
                a = stack.pop()
                b = stack.pop()
                res = int(a) * int(b)
                stack.append(res)
            elif t == '/':
                a = stack.pop()
                b = stack.pop()
                res = int(float(b) / a)
                stack.append(res)
            else:
                stack.append(int(t))

        return stack[0]