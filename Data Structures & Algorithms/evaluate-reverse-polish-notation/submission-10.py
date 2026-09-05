class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for x in tokens:
            if x not in ["+", "-", "/", "*"]:
                stack.append(int(x))
            else:
                if x == "+":
                    temp = stack.pop()
                    stack.append(stack.pop() + temp)
                elif x == "-":
                    temp = stack.pop()
                    stack.append(stack.pop() - temp)
                elif x == "/":
                    temp = stack.pop()
                    stack.append(int(stack.pop() / temp))
                elif x == "*":
                    temp = stack.pop()
                    stack.append(stack.pop() * temp)
        return stack.pop()
