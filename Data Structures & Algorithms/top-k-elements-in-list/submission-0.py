class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for x in nums:
            if x in hashmap:
                hashmap[x] += 1
            else:
                hashmap[x] = 1
        sorted_x = sorted(hashmap.items(), key = lambda item : item[1], reverse = True) [:k]
        return [x[0] for x in sorted_x]
