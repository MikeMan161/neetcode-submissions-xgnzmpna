class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # what if we use a frequency map/
        #keep track of largest frequency inside the window
        #window size - largest frequency = num of characters to replace
        #if num characters to replace is <= k, window is valid
        #update a length character to keep track of best length seen
        #when do we expand right?
        #we expand right, doing calculations till window is incorrect 
        #when do we shrink left?
        #shrink left until the window is valid again
        #when do we update the result
        #each time 


        left, right = 0, 0
        frequency = {}
        #{x:2, Y: 2}
        maxLength = 0
        #maxLength = 4

        while right < len(s):
            #ad character at s[right] to frequency
            if s[right] not in frequency:
                frequency[s[right]] = 1
            else:
                frequency[s[right]] += 1
            #check if valid
            #if not valid, iterate the left until window is valid (when window - max frequency <= k)
            while ((right - left) + 1) - max(frequency.values()) > k:
                #each iteration of left, decrement frequency[s[left]]
                frequency[s[left]] -= 1
                #iterate left
                left += 1
            #update maxLength
            if (right - left) + 1 > maxLength:
                maxLength = (right - left) + 1
            right += 1
        #return maxLength
        return maxLength
            
