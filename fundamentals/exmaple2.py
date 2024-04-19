"""
A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years.
Ask user for their salary and year of service and print the net bonus amount.
"""

service = int(input('Enter your service in year: '))
salary = float(input('Enter your salary: '))

if service > 5:
    bonus = salary * .05
    print("Your Bonus: ", bonus)
else:
    print("You are not Eligible for the bonus")

