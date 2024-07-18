# Manger salary- 2000 dollars
# Director Salary- 1800 dollars
# Employee Salary- 1000 dollars
# Intern Salary- 500 dollars

print("Enter Salary:")
Salary = int(input())

print("Salary = %0.2f" %Salary)
if Salary >= 1500 and Salary <= 2000:
    print("Your Position is Manager")
elif Salary >= 1200 and Salary <= 1500:
    print("Your Position is Director")
elif Salary >= 600 and Salary <=1000:
    print("Your position is Employee")
elif Salary >= 200 and Salary <= 600:
    print("Your Position is Intern")
elif Salary>= 150 and Salary <= 2000:
    print("Your Position is Cleaner")
else:
    print("Not Applicable")