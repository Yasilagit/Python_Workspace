noOfElement = int(input())
givenArray = list(map(int, input().split()))

numberOfPairs = 0
pairFoundElement = []
currentMatch = 0
for i in range(0, noOfElement, 1):
    if(givenArray[i] not in pairFoundElement):
        currentMatch = 1
        for j in range(0, noOfElement, 1):
            if(i != j and givenArray[i] == givenArray[j]):
                currentMatch += 1
        numberOfPairs += int(currentMatch / 2)
        pairFoundElement.append(givenArray[i])
        currentMatch = 0


print(numberOfPairs)
