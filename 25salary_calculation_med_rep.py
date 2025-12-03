'''write a program to calculate the salary of a medical representative considering the
sales bonus and incentives offered to him on the total sales.
if the sales exceed or equal to rs 1,00,000
follow the given values
basic=4000             #basic=4000
HRA=20% of basic       #HRA=10% of basic
DA=110% of basic       #DA=110% of basic
conveyance=500         #conveyance=500
incentive=10% of sales #incentive=4% of sales
BONUS=1000                #BONUS=500'''


# program to calculate the salary of a medical representative

sales = float(input("Enter the total sales of month: "))

if sales >= 100000:
    basic = 4000
    hra = 20 * basic / 100
    da = 110 * basic / 100
    conveyance = 500
    incentive = 10 * sales / 100
    bonus = 1000
else:
    basic = 4000
    hra = 10 * basic / 100
    da = 110 * basic / 100
    conveyance = 500
    incentive = 4 * sales / 100
    bonus = 500

gross_salary = basic + hra + da + conveyance + incentive + bonus

print("\n----- Salary Details -----")
print("Basic Salary        :", basic)
print("HRA                 :", hra)
print("DA                  :", da)
print("Conveyance          :", conveyance)
print("Incentive           :", incentive)
print("Bonus               :", bonus)
print("----------------------------")
print("Gross Salary        :", gross_salary)




