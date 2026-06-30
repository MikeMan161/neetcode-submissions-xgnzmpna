class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        valid = {")": "(", "}": "{", "]": "["}
        #Start iterating through the string
        for chars in s: 
            #if opening bracket, place in stack
            #if closing bracket, compare stack[-1] to valid[closing bracket]
            if chars not in valid:
                stack.append(chars)
            else:
                if stack and valid.get(chars) == stack[-1]:
                    stack.pop(-1)
                else:
                    return False
        if stack and s != '':
            return False
        else:
            return True
                #if true, pop stack
                #else, return false since the string is invalid