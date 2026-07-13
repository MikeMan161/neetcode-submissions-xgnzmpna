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
                    tempSum = stack.pop() + tempNum
                    stack.append(tempSum)
                elif nums == '-':
                    tempNum = stack.pop()
                    tempSum = stack.pop() - tempNum
                    stack.append(tempSum)
                elif nums == '*':
                    tempNum = stack.pop()
                    tempSum = stack.pop() * tempNum
                    stack.append(tempSum)
                elif nums == '/':
                    tempNum = stack.pop()
                    tempSum = int(stack.pop() / tempNum)
                    stack.append(tempSum)
        return stack.pop()

