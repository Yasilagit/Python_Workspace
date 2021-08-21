class Difference:
    def __init__(self, a):
        self.__elements = a
    maximumDifference=0
    def computeDifference(self):
        
        for i in range(0, len(self.__elements), 1):
            for j in range(1, len(self.__elements), 1):
                currentDifference = abs(self.__elements[i]-(self.__elements[j]))
                if (self.maximumDifference < currentDifference):
                    self.maximumDifference = currentDifference
        return self.maximumDifference

# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)

# class Difference:
#     maximumDifference = 0

#     def __init__(self, givenArray):
#         self.__elements = givenArray

#     def computeDifference(self):
#         for i in range(0, len(self.__elements), 1):
#             for j in range(1, len(self.__elements), 1):
#                 currentDifference = abs(self.__elements[i]-(self.__elements[j]))
#                 if (self.maximumDifference < currentDifference):
#                     self.maximumDifference = currentDifference
#         print(self.maximumDifference)


# noOfElements = int(input())
# givenArray = list(map(int, input().split()))
# difObject = Difference(givenArray)
# difObject.computeDifference()
