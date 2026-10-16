class TimeMap:

    def __init__(self):
        self.hashMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hashMap:
            self.hashMap[key] = []
        self.hashMap[key].append([timestamp,value])
        # print(self.hashMap)        

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.hashMap.get(key, [])
        l,r = 0, len(values)-1
        while l<=r :
            m = (l+r)//2  
            if values[m][0] <= timestamp:
                res = values[m][1] 
                l = m + 1
            else:
                r = m - 1
        return res
        
