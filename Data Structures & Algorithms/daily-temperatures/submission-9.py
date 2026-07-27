class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #monotonic stack but adding "local maximums"
        #iterating from right to left, adding numbers. 
        # add 1 when doing calculation for day
        stack = []
        right = len(temperatures) - 1
        result = [0] * len(temperatures)

        #loop to iterate from right to left
        while right >= 0:
            #start adding to stack
            #initialize stack for first iteration:
            if not stack:
                stack.append(right)
            #now we start the main loop. first, we check temp[right] and compare to top of stack
            # if it's greater than the top of stack, run a loop to pop all smaller numbers until
            #you find a greater value or the stack becomes empty. if you find a greater value, calc
            # result[i]. if empty, return nothing as the stack already has 0s in place
            #if less than, simply calculate result[i] then append to stack to keep local maximums
            else:
                if temperatures[right] < temperatures[stack[-1]]:
                    stack.append(right)
                    result[right] = stack[1] - right
                while stack and temperatures[right] >= temperatures[stack[-1]]:
                    stack.pop()
                if not stack:
                    stack.append(right)
                else:
                    result[right] = stack[-1] - right
                    stack.append(right)
            right -= 1
        return result
