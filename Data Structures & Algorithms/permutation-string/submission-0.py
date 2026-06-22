class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        # Initialize frequencies for s1 and the first window of s2
        s1_count = {}
        s2_count = {}
        
        for i in range(len(s1)):
            s1_count[s1[i]] = s1_count.get(s1[i], 0) + 1
            s2_count[s2[i]] = s2_count.get(s2[i], 0) + 1
            
        # If the very first window is a match, we are done
        if s1_count == s2_count:
            return True
            
        # Sliding Window
        left = 0
        for right in range(len(s1), len(s2)):
            # Add the new character on the right to our window
            s2_count[s2[right]] = s2_count.get(s2[right], 0) + 1
            
            # Remove the character on the left from our window
            s2_count[s2[left]] -= 1
            if s2_count[s2[left]] == 0:
                del s2_count[s2[left]] # Clean up 0 counts to make dict comparison easy
                
            left += 1
            
            # Check if the current window matches s1's frequency
            if s1_count == s2_count:
                return True
                
        return False


        