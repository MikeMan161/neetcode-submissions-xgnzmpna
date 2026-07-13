class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        tempNum = 0
        tempSum = 0
        for nums in tokens:
            if nums not in ['+', '-', '*', '/']:
                stack.append(int(nums))
            else:
                if nums == '+':
                    tempNum = stack.pop()
                    stack.append(stack.pop() + tempNum)
                elif nums == '-':
                    tempNum = stack.pop()
                    stack.append(stack.pop() - tempNum)
                elif nums == '*':
                    tempNum = stack.pop()
                    stack.append(stack.pop() * tempNum)
                elif nums == '/':
                    tempNum = stack.pop()
                    stack.append(int(stack.pop() / tempNum))
        return stack.pop()

