class Solution:

    from collections import Counter
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        counted = Counter(nums)

        return [num for num, freq in sorted(counted.items(), key=lambda item: item[1])[-k:]]
