class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        check = {"}": "{", "]": "[", ")": "("}

        for char in s:
            if char in check:
                if stack and stack[-1] == check[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        if stack:
            return False
        return True
