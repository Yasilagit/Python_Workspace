alicScore = []
bobScore = []


aliceTriplet = list(map(int, input().split()))
bobTriplet = list(map(int, input().split()))

for i in range(0,len(aliceTriplet),1):
    if(aliceTriplet[i] > bobTriplet[i]):
        alicScore.append(1)
    elif(aliceTriplet[i] != bobTriplet[i]):
        bobScore.append(1)

aliceFinalmark = 0
bobFinalMark = 0
for i in range(0,len(alicScore),1):
    aliceFinalmark += alicScore[i]
for i in range(0,len(bobScore),1):
    bobFinalMark += bobScore[i]

print(str(aliceFinalmark) + " " + str(bobFinalMark))
