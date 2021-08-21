noOfElements = int(input())
givenArray = list(map(int, input().split()))


def calculate(givenArray):
    totalValue = 0
    for i in range(0, len(givenArray), 1):
        totalValue += givenArray[i]
    return totalValue

print(calculate(givenArray))
