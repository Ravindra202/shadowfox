@@ -0,0 +1,44 @@
#Task1-Name with length
friends = ["Chandu", "Ravi", "Suresh", "Kiran", "Vamsi"]
result = []
for name in friends:
    result.append((name, len(name)))
print(result)

#Task2-Expence Tracker
your_expenses = {
        "Hotel": 1200,
        "Food": 800,
        "Transportation": 500,
        "Attractions": 300,
        "Miscellaneous": 200
    }
    
partner_expenses = {
        "Hotel": 1000,
        "Food": 900,
        "Transportation": 600,
        "Attractions": 400,
        "Miscellaneous": 150
    }
    
# Total expenses
your_total = sum(your_expenses.values())
partner_total = sum(partner_expenses.values())
print("Your total:", your_total)
print("Partner total:", partner_total)
if your_total > partner_total:
    print("You spent more")
elif partner_total > your_total:
    print("Your partner spent more")
else:
    print("Both spent equally")
max_diff = 0
max_category = ""
for key in your_expenses:
    diff = abs(your_expenses[key] - partner_expenses[key])
    if diff > max_diff:
        max_diff = diff
        max_category = key
print("Maximum difference in:", max_category)
print("Difference amount:", max_diff)
