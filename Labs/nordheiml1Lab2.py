class Customer:
    # creating customer class with required methods
    def __init__(self, name, oBalance):
        self.customerName = name
        self.openingBalance = oBalance
        self.closingBalance = self.calculateClosingBalance()
        self.customerType = self.determineCustomerType()

    def calculateClosingBalance(self):
        cBalance = float((self.openingBalance * .125) + self.openingBalance)
        return cBalance

    def determineCustomerType(self):
        cBalance = self.calculateClosingBalance()
        if cBalance > 0 and cBalance < 90000:
            return "Bronze"
        elif cBalance > 90000 and cBalance < 100000:
            return "Silver"
        elif cBalance > 100000 and cBalance < 150000:
            return "Gold"
        else:
            return "Diamond"

    def displayInfo(self):
        print(str(self.customerName) + "\t\t\t\t" + str(self.customerType) + "\t\t\t\t" + str(self.openingBalance) + "\t\t\t" + str((self.openingBalance * .125)) + "\t\t\t" + str(self.closingBalance))

numCustomers = int(input("Enter the number of customers you have in this bank: "))

#taking number of customers needed and creating a list to store them

customers = []

# taking input for opening balance and name

for i in range(numCustomers):
    name = input("Enter customer " + str(i + 1) + "'s name:")
    balance = float(input("Enter customer " + str(i + 1) + "'s opening balance:"))
    if balance > 50:
        balance = balance
    else:
        balance = float(input("Enter customer " + str(i + 1) + "'s opening balance:"))
    newCustomer = Customer(name, balance)
    customers.append(newCustomer)

print("Customer Name\t\tCustomer Type\t\tOpening($)\t\tInterest($)\t\tClosing($)")
print("***********************************************************************************")

#for customer in customers:
    #customer.displayInfo(customer)

#printing info using the displayInfo method
for i in range(len(customers)):
    customers[i].displayInfo()

print("***********************************************************************************")
