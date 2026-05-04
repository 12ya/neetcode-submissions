class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        arr = [n for n in nums]
        heapq.heapify(arr)
        for _ in range(len(arr) - k):
            heapq.heappop(arr)
        return arr[0]