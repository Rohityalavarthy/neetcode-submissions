class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        length = len(nums)
        new = [1]*length

        left = 1
        for i in range(length):
            new[i] *= left
            left *= nums[i]
        
        right = 1
        for j in range(length-1,-1,-1):
            new[j] *= right
            right *= nums[j]

        return new