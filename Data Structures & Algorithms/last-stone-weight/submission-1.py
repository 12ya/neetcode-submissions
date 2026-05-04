class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            f = -heapq.heappop(stones)
            s = -heapq.heappop(stones)
            if f - s > 0:
                heapq.heappush(stones, -(f-s))

        return -stones[0] if stones else 0