#!/usr/bin/python
# Luke Nordheim, CIT 383, Lab 1

# take input for the number of students and number of days. It also checks if they're positive
numStudents = int(input("Enter the number of students"))
if numStudents > 0:
    numStudents = numStudents
else:
    numStudents = int(input("Enter the number of students"))

numDays = int(input("Enter the number of days in the week"))
if numDays > 0:
    numDays = numDays
else:
    numDays = int(input("Enter the number of days in the week"))

# creation of all the lists we need
scriptingHours = []
mathHours = []
scriptAvg = []
mathAvg = []
mostSpent = []

# this method checks if the hours are in the correct range
def hourCheck(numHours):
    if numHours >= 0 and numHours <= 9:
        return True
    else:
        return False

# this method returns a string with the max hours, for some weird reason I kept getting the reverse of what it should
# be, I flipped the first sign
def maxHours(scriptingHours, mathHours):
    if sum(mathHours) < sum(scriptingHours):
        return "Math"
    elif sum(mathHours) == sum(scriptingHours):
        return "Same"
    else:
        return "Scripting"

# this method gives me the average hours
def average(hours):
    if len(hours) == 0:
        print("no input was given")
    else:
        avg = sum(hours) / len(hours)
        return avg

#this is for the final print statement
def finalPrint(scriptAvg, mathAvg, mostSpent):
    count = len(scriptAvg)
    print("Student\t\tAvg Script Time\t\tAvg Math Time\t\tMost Time Spent")
    print("-------\t\t---------------\t\t-------------\t\t---------------")
    for i in range(1, count + 1):
        print(str(i) + "\t"*4 + str(scriptAvg[i-1]) + "\t"*5 + str(mathAvg[i -1]) + "\t"*5 + str(mostSpent[i-1]))

# this double for loop fills my scripting and math hours list from input
for students in range(1, (numStudents + 1)):
    for days in range(1, numDays + 1):
        numHours = int(input("Day " + str(days) + " Enter number of hours spent on scripting for student " + str(students) + ": "))
        while not (hourCheck(numHours)):
            numHours = int(input("Day " + str(days) + " Enter number of hours spent on scripting for student " + str(students) + ": "))
        scriptingHours.append(numHours)

        numHours = int(input("Day " + str(days) + " Enter number of hours spent on math for student " + str(students) + ": "))
        while not (hourCheck(numHours)):
            numHours = int(input("Day " + str(days) + " Enter number of hours spent on math for student " + str(students) + ": "))
        mathHours.append(numHours)

    # here I am appending the average lists and calling the method average to get the average value
    scriptAvg.append(average(scriptingHours))
    mathAvg.append(average(mathHours))
    # here I am appending to mostSpent to get the max hours between subject
    mostSpent.append(maxHours(mathHours, scriptingHours))

    # we clear the lists for new students
    scriptingHours = []
    mathHours = []

finalPrint(scriptAvg, mathAvg, mostSpent)
print("-------\t\t---------------\t\t-------------\t\t---------------")
finalScriptingHours = int(sum(scriptAvg) / len(scriptAvg))
finalMathHours = int(sum(mathAvg) / len(mathAvg))
if finalScriptingHours > finalMathHours:
    mostTimeSpent = "Scripting"
elif finalScriptingHours == finalMathHours:
    mostTimeSpent = "Same"
else:
    mostTimeSpent = "Math"

print("Overall Avg. " + "\t" + str(finalScriptingHours) + "\t"*5 + str(finalMathHours) + "\t"*5 + mostTimeSpent)