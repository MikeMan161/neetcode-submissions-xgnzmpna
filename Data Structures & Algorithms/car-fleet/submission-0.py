class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = sorted(zip(position, speed))
        targetTime = []
        fleet_count = 0
        i = len(position) - 1
        maxTime = 0
        for position, speed in pairs:
            targetTime.append((target - position) / speed)
        while i >= 0:
            if targetTime[i] > maxTime:
                maxTime = targetTime[i]
                fleet_count += 1
            i -= 1
        return fleet_count




#            pairs = ((0,1), (1,2), (4,2), (7,1))
#            targetTime = [10, 4.5, 3, 3]
