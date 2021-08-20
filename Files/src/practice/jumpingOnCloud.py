# some one else solution


# Solution 1
# def jumpingOnClouds(c):
#     x,y = 0,0
#     while x<len(c)-2:
#         x = x+1 if c[x+2] else x+2
#         y+=1
#     if x<len(c)-1:
#         y+=1
#     return y
# c = list(map(int,input().split()))
# print(jumpingOnClouds(c))

# Yasila solution
# a = list(map(int, input().split()))
# outerLoop = 0
# innerLoop = outerLoop+1
# isMissed = False
# jump = 0

# while (outerLoop < len(a)):
#     if(innerLoop < len(a)-1 and a[outerLoop] == 0 and a[innerLoop] == 0 and a[innerLoop + 1] == 0 and isMissed == False):
#         jump += 1
#         outerLoop = innerLoop+1
#         innerLoop = outerLoop+1
#         isMissed = False
#     elif(a[outerLoop] == 0 and a[innerLoop] == 0):
#         jump += 1
#         outerLoop = innerLoop
#         innerLoop = outerLoop+1
#         isMissed = False
#     elif(a[outerLoop] == 0 and a[innerLoop] != 0):
#         innerLoop += 1
#         isMissed = True
#     if(innerLoop == len(a)):
#         outerLoop = innerLoop

# print(jump)
