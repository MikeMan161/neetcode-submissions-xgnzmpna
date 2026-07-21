class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return "" 
        window = {}
        frequency = {}
        have = 0
        res = [-1, -1]
        resLen = float('inf')
        left, right = 0, 0
        #fill frequency map
        for i in range(len(t)):
            if t[i] in frequency:
                frequency[t[i]] += 1
            else:
                frequency[t[i]] = 1
        need = len(frequency)
        
        # Open window
        while right < len(s):
            # check if s[right] in frequency, add to window if pass
            if s[right] in frequency:
                if s[right] in window:
                    window[s[right]] += 1
                else:
                    window[s[right]] = 1
                # if frequency in window == frequency map, increment have
                if window[s[right]] == frequency[s[right]]:
                    have += 1
            # when have == need, start shrinking window
            while have == need:
                #update result if right - left + 1 < reslen
                if right - left + 1 < resLen:
                    resLen = right - left + 1
                    res = [left, right]
                #decrease count of s[left] in window
                if s[left] in frequency:
                    window[s[left]] -= 1
                    # if s[left] in frequency and window[s[left]] < frequency[s[left]]
                    # decrement have
                    if window[s[left]] < frequency[s[left]]:
                        have -= 1
                left += 1
            right += 1

        return s[res[0]: res[1]+1]