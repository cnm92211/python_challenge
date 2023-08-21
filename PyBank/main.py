import csv
from pathlib import Path

# Read CSV file
input_file = Path("Resources/budget_data.csv")
output_file = Path("financial_analysis.txt")

total_months = 0
total_profitloss = 0
profit_loss = []
previous_profit_loss = 0
month_of_change = []
profit_loss_change = 0
greatest_decrease = ["", 100000000]
greatest_increase = ["", 0]
change_list = []
profit_loss_average = 0


with input_file.open() as csvfile:
    csv_dict = csv.DictReader(csvfile)

    for row in csv_dict:

        #The total number of months included in the dataset
        total_months += 1

        #The net total amount of "Profit/Losses" over the entire period
        total_profitloss = total_profitloss + int(row["Profit/Losses"])

        #The changes in "Profit/Losses" over the entire period, and then the average of those changes
        profit_loss_change = float(row["Profit/Losses"])- previous_profit_loss
        previous_profit_loss = float(row["Profit/Losses"])
        change_list = change_list + [profit_loss_change]
        month_of_change = [month_of_change] + [row["Date"]]
       

        #The greatest increase in profits (date and amount) over the entire period
        if profit_loss_change>greatest_increase[1]:
            greatest_increase[1]= profit_loss_change
            greatest_increase[0] = row['Date']

        #The greatest decrease in profits (date and amount) over the entire period
        if profit_loss_change<greatest_decrease[1]:
            greatest_decrease[1]= profit_loss_change
            greatest_decrease[0] = row['Date']
    profit_loss_average = sum(change_list)/len(change_list)

print(total_months)
print(total_profitloss)
print(greatest_increase)
print(greatest_decrease)
print(profit_loss_average)


report = f"""Financial Analysis
----------------------------
Total Months: {total_months}
Total: ${total_profitloss}
Average Change: ${profit_loss_average:.2f}
Greatest Increase in Profits: {greatest_increase}
Greatest Decrease in Profits: {greatest_decrease}
"""

# Print to Terminal Box
print(report)

#Spit Out to Text File
with open("Analysis/financial_analysis.txt", "w") as txtfile:
    txtfile.write(report)