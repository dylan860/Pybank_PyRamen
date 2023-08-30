import csv
from pathlib import Path
budget_path = Path('./Resources/budget_data.csv')
total_months = 0

total_profit = 0
greatest_increase = int(0)
greatest_decrease = int(0)
greatest_increase_date = None
greatest_decrease_date = None
pnl = []
# Opening CSV File 
with open(budget_path, newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    next(reader)
    for row in reader:
        total_months +=1
        pnl.append(row)
# Calculating the Changes in Profit/Loss
# Separating the dates and profits data
# Calclating the increase and decrease of the portfolio and storing it in a list 
current_num = 0
last_num = 0
changes = []
change_and_date = []


for i in pnl:
    if current_num == 0:
        current_num = i[1]
    elif current_num != 0:
        last_num = current_num
        current_num = i[1]
        changes = (int(current_num) - int(last_num))
        change_date = i[0]
        change_and_date.append([change_date,changes])
# Calculating the Total gain
for i in pnl:
    total_profit += int(i[1])
# Calculating the Average Change
change_count = 0
total_change = 0
for i in change_and_date:
    total_change += i[1]
    change_count += 1

avg_change = total_change / change_count
#  Greatest Increase in Profits
for i in change_and_date:
    if i[1] > greatest_increase:
        greatest_increase = i[1]
        greatest_increase_date = i[0]

        
# Greatest Decrease in Profits
for i in change_and_date:
    if i[1] < greatest_decrease:
        greatest_decrease = i[1]
        greatest_decrease_date = i[0]
# Printing all outputs

print('Financial Analysis')
print('-------------------')

print(f'Total Months: {total_months}')
print(f'Total: ${total_profit}')
print(f'Average Change: ${round(avg_change,2)}')
print(f'Greatest Increase: ${greatest_increase} on {greatest_increase_date}')
print(f'Greatest Decrease: ${greatest_decrease} on {greatest_decrease_date}')