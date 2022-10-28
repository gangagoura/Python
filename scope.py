lass Difference:
    def __init__(self, a):
        self.__elements = a


    def computeDifference(self):
        maxDiff = 0
        arr = self.__elements
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                if abs(arr[j] - arr[i]) > maxDiff:
                    maxDiff = abs(arr[j] - arr[i])
        self.maximumDifference = maxDiff



_ = raw_input()
a = [int(e) for e in raw_input().split(' ')]

d = Difference(a)
d.computeDifference()

print d.maximumDifference
