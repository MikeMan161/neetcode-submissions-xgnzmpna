class Solution:
    def isValid(self, s: str) -> bool:
        #use a stack to keep track of the opening brackets
        #key value pairs
        hashmap = {")": "(", "}": "{", "]": "["}
        stack = []
        
        for x in s:
            #if not in hashmap, that means it's an opening bracket, append to stack
            if x not in hashmap:
                stack.append(x)

            #if it is (else statement), then it's a closing bracket, and we must compare x to the value
            else:
                #if the top of stack is equal to the value in the hashmap, pop stack. else, return false
                if stack and hashmap[x] == stack[-1]:
                    stack.pop()
                else:
                    return False
        if stack:
            return False
        else:
            return True