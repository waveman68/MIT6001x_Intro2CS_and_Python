# Test Case 1:

balance = 4213
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

# Test Case 2:
# balance = 4842
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

# ================================
# Code to pay only minimum payment
# ================================
totalPaid = 0
remainingBalance = balance
unpaidBalance = balance
monthlyInterestRate = annualInterestRate / 12.0

for i in range(1, 13):
    minimumMonthlyPayment = monthlyPaymentRate * remainingBalance
    unpaidBalance = remainingBalance - minimumMonthlyPayment
    remainingBalance = unpaidBalance * (1 + monthlyInterestRate)

    totalPaid += minimumMonthlyPayment
    print('Month: %u' % i)
    print('Minimum monthly payment: %.2f' % minimumMonthlyPayment)
    print('Remaining balance: %.2f' % remainingBalance)

print('Total paid: %.2f' % totalPaid)
print('Remaining balance: %.2f' % remainingBalance)

print('=======')

# ================================
# Code to pay in 12 mos. to the nearest $10
# ================================
balance = 3926
annualInterestRate = 0.2

monthlyPayment = 0  # initialize
remainingBalance = balance
unpaidBalance = balance
monthlyInterestRate = annualInterestRate / 12.0

while remainingBalance > 0:
    monthlyPayment += 10
    remainingBalance = balance
    for i in range(1, 13):
        unpaidBalance = remainingBalance - monthlyPayment
        remainingBalance = unpaidBalance * (1 + monthlyInterestRate)

print('Lowest Payment: %u' % monthlyPayment)

print('=======')

# ================================
# Code to pay in 12 mos. using bisection
# ================================

balance = 999999
annualInterestRate = 0.18

monthlyPayment = 0  # initialize
remainingBalance = balance
unpaidBalance = balance

monthlyInterestRate = annualInterestRate / 12.0
monthlyPaymentLB = balance / 12
monthlyPaymentUB = (balance * (1 + monthlyInterestRate) ** 12) / 12.0

while monthlyPaymentUB - monthlyPaymentLB > 0.01:
    monthlyPayment = (monthlyPaymentLB + monthlyPaymentUB) / 2.0
    remainingBalance = balance
    for i in range(1, 13):
        unpaidBalance = remainingBalance - monthlyPayment
        remainingBalance = unpaidBalance * (1 + monthlyInterestRate)
    print('Remaining Balance with a monthly payment of %.2f: %.2f' % (monthlyPayment, remainingBalance))
    if remainingBalance > 0:
        monthlyPaymentLB = monthlyPayment
    elif remainingBalance < 0:
        monthlyPaymentUB =monthlyPayment

monthlyPayment = round(monthlyPayment, ndigits=2)
print('Lowest Payment: %.2f' % monthlyPayment)
