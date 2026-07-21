class TimeMap:

    def __init__(self):
        #initialize the dictionary
        self.hashmap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        #insert the values into the hashmap
        #the key-value goes like this: [key: [timestamp, value]]
        if key not in self.hashmap:
            self.hashmap[key] = []
        self.hashmap[key].append([timestamp, value])


    def get(self, key: str, timestamp: int) -> str:
        #This is where we search the hashmap to find either the given timestamp
        #or the largest timestamp less than timestamp, aka left boundary binary search
        if key not in self.hashmap:
            return ""
        timeList = list(self.hashmap[key])
        left = 0
        right = len(timeList) - 1
        result = ""
        while left <= right:
            mid = left + (right - left) // 2
            if timeList[mid][0] == timestamp:
                return timeList[mid][1]
            if timeList[mid][0] <= timestamp:
                result = timeList[mid][1]
                left = mid + 1
            else:
                right = mid - 1
        return result




        
