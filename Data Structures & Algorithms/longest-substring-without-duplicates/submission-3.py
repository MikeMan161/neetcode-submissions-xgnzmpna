class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #how do we track that every character is unique
        #frequency map would help 
        #the window is valid when every character's frequency is equalto 1, aka unique
        #if we come across a character that's already in the frequency map, we know that
        #the window would become invalid. 
        #as soon as the window is invalid, shrink the left until it's valid again
        #return/save the length, keep going.

        #iterate variables
        left, right = 0, 0
        frequency = {}
        #{a: 1, b: 1,c: 1}
        maxLength = 0
        #start the loop
        
        while right <= len(s) - 1:
            #check the variable at the right index. if not in frequency, add it
            if s[right] not in frequency:
                frequency[s[right]] = 1
            #if it is in frequency, window is now invalid
            else:
                frequency[s[right]] += 1
                #loop to shrink the window using left pointer
                #we know the specific variable that caused the window to be invalid s[right]
                while frequency[s[right]] > 1:
                    #so keep shrinking until frequency[s[right]] == 1
                    #when it's 1 again, we know the window is valid
                    frequency[s[left]] -= 1
                    left += 1
            #save the length between right and left as the size of substring
            if (right - left) + 1 > maxLength:
                maxLength = (right - left) + 1
                #2
            #iterate right pointer
            right += 1
        return maxLength
