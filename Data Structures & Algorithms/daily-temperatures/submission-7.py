class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)
        i = len(temperatures) - 1
        while i >= 0:
            if not stack:
                stack.append(i)
                result[i] = 0
            else:
                if temperatures[stack[-1]] > temperatures[i]:
                    result[i] = stack[-1] - i
                    stack.append(i)
                while stack and temperatures[stack[-1]] <= temperatures[i]:
                    stack.pop()
                if not stack:
                    result[i] = 0
                    stack.append(i)
                else:
                    result[i] = stack[-1] - i
                    stack.append(i)
            i -= 1
        return result





            