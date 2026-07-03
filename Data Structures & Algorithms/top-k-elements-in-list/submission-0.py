class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = Counter(nums)
        
        return [element for element, count in frequency.most_common(k)]


