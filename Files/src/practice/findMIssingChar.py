def missingCharacters(givenArray):

    char = ['a', 'b', 'c', 'd', 'd', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z']
    number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    outPut = []
    givenArray = list(input())
    for i in range(0, len(number), 1):
        if number[i] not in givenArray:
            outPut.append(number[i])
    for i in range(0, len(char), 1):
        if char[i] not in givenArray:
            outPut.append(char[i])
    return  ''.join(outPut)
