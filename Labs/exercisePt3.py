class Owner:
    def __init__(self, pAddress, pValue):
        self.propertyAddress = pAddress
        self.priorValue = pValue
        self.taxableAmt = 0
        self.taxDue = self.taxesDue()

    # class methods
    def newValue(self):
        new_val = self.priorValue + self.priorValue * 0.027
        return new_val

    def taxesDue(self):
        self.taxableAmt = self.newValue() - 25000
        nThousands, rem = divmod(self.taxableAmt, 1000)
        if rem != 0:
            nThousands += 1

        tax = nThousands * 10.03
        return tax

    def displayResults(self):
        print("street address: %s" % self.propertyAddress)
        print("last accessed value: $%.2f" % self.priorValue)
        print("current value: $%.2f " %self.newValue())
        print("exemption: $%.2f" % 25000)
        print("taxable value: $%.2f" % self.taxableAmt)
        print("tax rate: $%.2f" % 10.03)
        print("taxes due: $%.2f" % self.taxDue)

owners = []
for i in range(2):
    address = input("Enter the address: {i + 1}: ")
    value = float(input("Enter the previous year's value for property {i+1}"))
    newOwn = Owner(address, value)
    owners.append(newOwn)

for own in owners:
    own.displayResults(owners)

