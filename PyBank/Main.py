import os
import csv
from tkinter.tix import INCREASING

#-----------------------------------------------------
# Set working directory to where this Python file is
os.chdir(os.path.dirname(__file__))

budget_data_csv = os.path.join("Resources", "budget_data.csv")
output = os.path.join("analysis", "budget_analysis.txt")

#define list
profit_and_loss_changes = []
increase_month = ""
decrease_month = ""

#define variables
count_months = 0
total_profit = 0
start_profit = 0
net_change_profit = 0
max_increase = 0
max_decrease = 1000000000

# Open and read csv
with open(budget_data_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

# Read the header row and first row
    csv_header = next(csv_reader )

    first_row = next(csv_reader)
    count_months += 1
    total_profit = total_profit + int(first_row[1])
    start_profit = int(first_row[1])

# Read through each row of data after the 1st row
    for row in csv_reader:
        # Count of months
        count_months += 1

        #calculate total profit
        total_profit = total_profit + int(row[1])

        #calculate average month to month change in profit
        end_profit = int(row[1])
        monthly_profit_and_loss_changes = end_profit - start_profit
        start_profit = int(row[1])

        #store/assign monthly chanages to a list and calculate net chanegs in profit
        profit_and_loss_changes.append(monthly_profit_and_loss_changes)

        #calculate average change in profit

        net_change_profit = round(sum(profit_and_loss_changes)/len(profit_and_loss_changes),2)

        #calculate greatest increase and decrease in profits
        if monthly_profit_and_loss_changes > max_increase:
            max_increase = monthly_profit_and_loss_changes
            increase_month = row[0]


        if monthly_profit_and_loss_changes < max_decrease:
            max_decrease = monthly_profit_and_loss_changes
            decrease_month = row[0]

#Print and create output file

output_file=(f"Financial Analysis\n"
f"----------------------------\n"
f"Total Months: {count_months}\n"
f"Total: ${total_profit}\n"
f"Average Change: ${net_change_profit}\n"
f"Greatest Increase in Profits: {increase_month} (${max_increase})\n"
f"Greatest Decrease in Profits: {decrease_month} (${max_decrease})\n")

print(output_file)

with open(output, "w") as output_txt:
    output_txt.write(output_file)