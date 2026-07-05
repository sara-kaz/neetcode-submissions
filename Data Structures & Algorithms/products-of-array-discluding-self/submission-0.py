class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
       
        out = [1]* len(nums)
        i = 0

        for indx, num in enumerate(nums):
            before_mult, after_mult = 1, 1

            for i in range(0, indx):
                before_mult *= nums[i]
            for j in range(indx+1, len(nums)):
                after_mult *= nums[j]

            out[indx] = before_mult * after_mult

        
        return out
            


        