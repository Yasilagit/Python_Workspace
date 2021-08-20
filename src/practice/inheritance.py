class Person:
    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber

    def printPerson(self):
        print("Name: " + self.lastName + "," + self.firstName)
        print("ID:" + self.idNumber)


class Student(Person):
    def __init__(self, firstName, lastName, idNumber, scores):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber
        self.scores = scores

    def calculate(self):
        noOfMarks = len(self.scores)
        total = 0
        for i in range(0,  noOfMarks, 1):
            total += int(self.scores[i])
        avg = total/noOfMarks
        if (avg >= 90 and avg <= 100):
            return "O"
        elif (avg >= 80 and avg < 90):
            return "E"
        elif (avg >= 70 and avg < 80):
            return "A"
        elif(avg >= 55 and avg < 70):
            return "P"
        elif(avg >= 40 and avg < 55):
            return "D"
        elif(avg < 40):
            return "T"


givenInput = input().split()
firstName = givenInput[0]
lastName = givenInput[1]
idNumber = givenInput[2]
noScore = int(input())
scores = list(map(int, input().split()))
isMarkCorrect = True

for mark in scores:
    if (mark > 100 or mark <= 0):
        isMarkCorrect = False
        break

if(isMarkCorrect and len(firstName) < 7 and len(lastName) < 7 and len(scores) <= noScore):
    student = Student(firstName, lastName, idNumber, scores)
    student.printPerson()
    print("Grade: " + student.calculate())
