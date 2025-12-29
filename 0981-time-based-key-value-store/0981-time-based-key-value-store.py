class TimeMap(object):

    def __init__(self):
        self.store = {} # k: list of lists [value, timestamp]

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        if key not in self.store:
            self.store[key]=[]
        self.store[key].append([value, timestamp])

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        result = ""
        values = self.store.get(key, [])
        low = 0
        high = len(values)-1
        while low<=high:
            mid = (low+high)//2
            if timestamp>=values[mid][1]:
                result = values[mid][0]
                low = mid+1
            else:
                high = mid-1

        return result
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)