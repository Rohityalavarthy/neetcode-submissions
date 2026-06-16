class MedianFinder:

    def __init__(self):
        self.data = []

    def addNum(self, num: int) -> None:
        self.data.append(num)
        self.data.sort()

    def findMedian(self) -> float:
        
        length = len(self.data)

        if length % 2 == 0:
            return (self.data[(length//2)-1] + self.data[length//2])/2
        else:
            return self.data[(length//2)]