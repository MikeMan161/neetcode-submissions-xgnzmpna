class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        i = len(temperatures) - 1
        result = [0] * int(len(temperatures))

        while i >= 0:
            while stack and temperatures[i] >= temperatures[stack[-1]]:
                stack.pop()

            if not stack:
                stack.append(i)
                i -= 1
                continue

            if temperatures[i] < temperatures[stack[-1]]:
                result[i] = stack[-1] - i
            
            stack.append(i)
            i -= 1
        return result
