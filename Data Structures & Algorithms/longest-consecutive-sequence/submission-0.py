class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        tempseq = 0
        Output = 0
        i = 0
        "this outer loop will go through each value in numset from index 0 - (n-1)"
        for x in numset:
            """
            this if checks if there is a number in the dataset before this number.
            if there is, then it will skip this index. if not, it will start counting the
            sequence
            """
            if (x - 1) not in numset:
                tempnum = x
                tempseq = 1
                "now we can use a while loop to keep looping while x+1 is in dataset"
                while tempnum + 1 in numset:
                    tempseq += 1
                    tempnum += 1
                if tempseq >= Output:
                    Output = tempseq
                    tempseq = 0
            else:
                continue  
        return Output
