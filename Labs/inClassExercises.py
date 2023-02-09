#break / pass / tuples?

# method that checks if the number is prime

def primeNumber(num):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                print(num, "is not prime.")
                break
            else:
                print(num, "is prime.")
                break
    else:
        print("Number is not positive")

primeNumber(6)
primeNumber(10)
primeNumber(11)
primeNumber(13)
primeNumber(21)
primeNumber(28)
primeNumber(61)

# method that checks if numbers are perfect
# perfect numbers are numbers that the factors of that number add up to itself, examples are 6 and 28

def perfNumber(num):
    totalFactors = 0

    for i in range(1, num):
        if num % i == 0:
            totalFactors = totalFactors + i
    if totalFactors == num:
        return True
    else:
        return False

print(perfNumber(5))  #false
print(perfNumber(6))  #true
print(perfNumber(28))  #true

#method that returns factorial

def factorial(num):
    prod = 1
    for i in range(1, num + 1):
        prod *= i
    return prod

userNumber = int(input("Enter the number of interest: "))

if primeNumber(userNumber):
    print("%d is a prime number" % userNumber)
else:
    print("%d is not a prime number" % userNumber)

if perfNumber(userNumber):
    print("%d is a perfect number" % userNumber)
else:
    print("%d is not a perfect number" % userNumber)

isPrimeStr = " is prime" if primeNumber(userNumber) else " is not prime"
isPerfectStr = " is perfect" if perfNumber(userNumber) else " is not perfect"

print("%d %s" % (userNumber, isPrimeStr))

class Student:
    def __init__(self, firstName, lastName):
        self.first_name = firstName
        self.last_name = lastName

    def getFullName(self):
        return self.first_name + " " +  self.last_name

class CIT383Student:
    def __init__(self):
        pass

# use the class

# 3 students

myStudents = []

for i in range(3):
    firstN = input("Enter the first name of the student {i + 1} : ")
    LastN = input("Enter the last name of the student {i + 1} : ")
    stdObject = Student(firstN, LastN)

    myStudents.append(stdObject)

for std in myStudents:
    print(std.getFullName())


