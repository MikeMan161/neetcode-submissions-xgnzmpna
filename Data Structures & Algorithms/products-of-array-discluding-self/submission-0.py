"""
So this is asking me to create an array where each entry is the product of all the elements
of the original array except for the number in that same index

original = [1,2,3]
answer = [(2 x 3), (1 x 3)] = [6, 3]

initial plan:
    Loop through the list, have a counter variable keeping track of the index i want to skip
    counter = 0
    output = []
    for x in nums:

New plan:
    We create 2 arrays. 
    for the first array, we iterate through the array and store the values of the products
    of each entry to the left
    example:
    a = [1,2,3,4]
    leftProduct = [(1), (1), (1x2), (1x2x3)]

    then, we can use the reverse function to get the same thing but from right to left
    i'll use splicing to have a seperate reverse array
    
    b = a[::-1]
    b is now [4,3,2,1]
    rightProduct = [(1), (4), (4x3), (4x3x2)]

    you want to exclude i, so for leftProduct, its not [(1, 1x2)], its [(1), (1)] because
    for the first entry there's nothing to the left, so 1 is the default (since 0 could
    cause a mult error) and entry 2 would be 1 because we exclude 1 (2 in this case) which 
    leaves it with just 1 (the value, not the default)

    now we multiply each entry of leftproduct and rightproduct to get the answer.
    iterate backwards through rightproduct
    each entry will contain the product of each element without i
        """
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        temp = 1
        leftProduct = [1] * len(nums)
        rightProduct = [1] * len(nums)
        for x in range(1, len(nums)):
            temp = temp * nums[x - 1]
            leftProduct[x] = temp
        temp = 1
        for i in range(len(nums)-2, -1, -1):
            temp = temp * nums[i+1]
            rightProduct[i] = temp
        output = [val1*val2 for val1,val2 in zip(leftProduct, rightProduct)]
        return output

            
