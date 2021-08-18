
leftDiagnolTotal = 0
rightDiagnolTotal = 0
diognalDiff = 0
givenList = []
noOfElemenets = int(input())
for i in range(0, noOfElemenets, 1):
    givenList.append(list(map(int, input().split())))

# find left diognal count
for i in range(0, len(givenList), 1):
    leftDiagnolTotal += givenList[i][i]

    # find left diognal count
columCounter = len(givenList)
for i in range(0, len(givenList), 1):
    rightDiagnolTotal += givenList[i][columCounter-1]
    columCounter -= 1
print(abs(leftDiagnolTotal - rightDiagnolTotal))
