# Python Business Income Analysis
# Project 1 - Plan A Portfolio

income = {
    "Monday": 120,
    "Tuesday": 145,
    "Wednesday": 98,
    "Thursday": 160,
    "Friday": 175,
    "Saturday": 210,
    "Sunday": 130
}

# Calculate total and average income
total_income = sum(income.values())
average_income = total_income / len(income)

print("=== Business Income Analysis ===")
print("Total income:", total_income)
print("Average daily income:", round(average_income, 2))

# Find highest income day
highest_day = max(income, key=income.get)
highest_income = income[highest_day]

print("Highest income day:", highest_day)
print("Highest income:", highest_income)

# Find lowest income day
lowest_day = min(income, key=income.get)
lowest_income = income[lowest_day]

print("Lowest income day:", lowest_day)
print("Lowest income:", lowest_income)

# Analyze good days
count = 0
good_income = 0

for day, amount in income.items():
    if amount >= 150:
        print(f"{day}: €{amount} - Good Day")
        count = count + 1
        good_income = good_income + amount
    else:
        print(f"{day}: €{amount} - Low Day")

print("Number of good days:", count)
print("Income from good days:", good_income)
