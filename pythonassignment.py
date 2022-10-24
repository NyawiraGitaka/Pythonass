for number in range (1, 31):
    if number % 2 == 0:
       print(f"Even {number}") 

for number in range (1, 31):
    if number % 2 != 0:
       print(f"Odd {number}") 
        
number = 2
while number <= 31:
    print(number)
    number = number + 2

funding = 50000
marketing = funding * (25/100) 
operating = funding * (50/100)
remainingbal = funding - (marketing + operating)

print("\nIncome and Expense Statement - Ahmed")
print(f"\nFunding: {funding}")
print("\nExpenses")
print(f"Marketing Expense: {marketing}")
print(f"Operating Expense: {operating}")
print(f"\nRemianing Balance: {remainingbal}")

print(f"\nAhmed can acquire {remainingbal/5}) customers with a budget of {remainingbal}")

