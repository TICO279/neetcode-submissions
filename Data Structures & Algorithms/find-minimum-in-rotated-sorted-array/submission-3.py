class Solution:
    def findMin(self, nums: List[int]) -> int:
        #Were gonna implement a binary search here
        if len(nums) == 1:
            return nums[0]

        L = 0
        R =  len(nums)-1

        while L < R:
            midpoint = (L+R) // 2

            #Scenario 1, the minimum is the next value given its smaller
            #and its supposed to be originally a sorted array
            #so the value should be bigger
            if nums[midpoint] > nums[midpoint + 1]:
                return nums[midpoint + 1]

            #Scenario 2, the midpoint is smaller than the number before
            #Given its sorted originally, the midpoint should be the minimum
            if nums[midpoint] < nums[midpoint - 1]:
                return nums[midpoint]

            #Our base case
            if nums[midpoint] < nums[R] and nums[midpoint] > nums[L]:
                return nums[0]
            #In the case that the left part is sorted, we look on the right
            if nums[midpoint] > nums[L]:
                L = midpoint + 1
            #In the case that the right part is sorted, we look on the left
            if nums[midpoint] < nums[R]:
                R = midpoint - 1
        
            

            
