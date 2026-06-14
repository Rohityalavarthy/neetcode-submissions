class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            m = (left + right) // 2

            if nums[m] == target:
                return m

            # Left half is sorted
            if nums[left] <= nums[m]:
                if nums[left] <= target < nums[m]:  # target in sorted left half
                    right = m - 1
                else:                                # target in right half
                    left = m + 1

            # Right half is sorted
            else:
                if nums[m] < target <= nums[right]:  # target in sorted right half
                    left = m + 1
                else:                                 # target in left half
                    right = m - 1

        return -1