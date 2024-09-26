# Exercise 1 - Bug Collector

# total_bugs = 0
# for day in range(1, 8):
#     bugs = int(input(f"Enter the bugs collected on day {day}: "))
#     total_bugs += bugs
# print(f"You collected a total of {total_bugs} bugs.")

# ---------------------------------------------------------------------------

# Exercise 2 - Calories Burned

# calories_per_min = 4.2
# total_burned = 0
#
#
# for calorie in range(10, 30, 5):
#     calories_burned = calories_per_min * calorie
#     total_burned += calories_burned
#     print(f"In {calorie} mins you burned {total_burned:.1f} calories.")
# print(f"You burned a total of {total_burned} calories.")
    
# ---------------------------------------------------------------------------

# Exercise 3 - Budget Analysis

# budget_amount = float(input("What is this month's budget? "))
# total_expenses = 0
#
# while True:
#     expense = input("Enter an expense (type 'done' to finish): ").lower()
#
#     if expense == "done":
#         break
#
#     expense = float(expense)
#     total_expenses += expense
#
# difference = budget_amount - total_expenses
#
# if difference > 0:
#     print(f"Good Job! You are under your budget by ${difference:.2f}.")
# elif difference < 0:
#     print(f"You are over budget by ${-difference:.2f}.")
# else:
#     print("You are exactly on budget.")

# ---------------------------------------------------------------------------

# Exercise 4 - Distance Traveled

# speed = int(input("What is the speed of the vehicle in mph? "))
# hours = int(input("How many hours has is traveled? "))
#
#
# print(f"Hour\tDistance Traveled")
# for hour in range(1, hours + 1):
#     distance = speed * hour
#     print(f"{hour}\t{distance}")

# ---------------------------------------------------------------------------

# Exercise 5 - Average Rainfall

# total_rainfall = 0
# num_of_months = 0
#
# years = int(input("Number of years: "))
#
# for year in range(1, years + 1):
#     print(f"Year: {year}")
#     for month in range(1, 13):
#         inches_rainfall = int(input(f"How many inches of rainfall was there for month {month}? "))
#         total_rainfall += inches_rainfall
#         num_of_months += 1
#
# average_rainfall = total_rainfall / num_of_months
#
# print(f"Total number of months: {num_of_months}")
# print(f"Out of {years} years there was a total of {total_rainfall} inches of rainfall.")
# print(f"Average rainfall per month: {average_rainfall:.2f}")

# ---------------------------------------------------------------------------

# Exercise 6 - Celsius to Fahrenheit Table

# print(f"Celsius\tFarenheit")
# for temp in range(0, 21):
#     f_conversion = (9 / 5) * temp + 32  
#     print(f"{temp}C\t{f_conversion:.2f}F")

# ---------------------------------------------------------------------------

# Exercise 7 - Pennies for Pay

# salary = 0.01
# total = 0
# days = int(input("Enter a number of days: "))
#
# print(f"Days\tSalary")
# for day in range(1, days + 1):
#     print(f"{day}\t${salary:.2f}")
#     total += salary
#     salary *= 2
# print(f"Total over {days} days is: ${total:.2f}")

# ---------------------------------------------------------------------------

# Exercise 8 - Sum of Numbers

# total = 0
#
# while True:
#     positive_num = int(input("Enter a positive number: "))
#
#     if positive_num < 0:
#         break
#
#     total += positive_num
#
# print(f"The total is {total}.")

# ---------------------------------------------------------------------------

# Exercise 9 - Ocean Levels

# ocean_lvl_year = 1.6
# ocean_risen = 0
#
# print(f"Year\tMilimeters Per Year")
# for year in range(1, 25 + 1):
#     ocean_risen = ocean_lvl_year * year 
#     print(f"{year}\t{ocean_risen:.2f}")
# print(f"The ocean level went up by {ocean_risen:.2f} in 25 years.")

# ---------------------------------------------------------------------------

tuition = 8000
tuition_increase = 0.03

print(f"Year\tTuition Increase")
for year in range(1, 5 + 1):
    print(f"{year}\t${tuition:.2f}")
    increase = tuition * tuition_increase
    tuition += increase 



