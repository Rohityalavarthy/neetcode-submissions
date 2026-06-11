class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        def area(left, right):
            return int(min(heights[left], heights[right])*(right-left))

        left = 0
        right = len(heights)-1
        maximum = 0

        while left < right:

            maximum = max(area(left, right), maximum)

            if heights[left] <= heights[right]:
                left += 1

            else:
                right -=1

        return maximum