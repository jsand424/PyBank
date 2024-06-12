# Modules
import os
import csv

#Total Months and Total Profit and Loss
# Set path for file
csvpath = os.path.join("Resources", "budget_data.csv")

def count_months_and_total_profit_losses(csvpath):
    total_months = 0
    total_profit_losses = 0.0
    
    with open(csvpath, mode='r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            total_months += 1
            total_profit_losses += float(row["Profit/Losses"])
    
    return total_months, total_profit_losses

# Replace 'path_to_your_csv_file.csv' with the actual path to your CSV file
total_months, total_profit_losses = count_months_and_total_profit_losses(csvpath)

print(f"Total number of months: {total_months}")
print(f"Net total amount of Profit/Losses: {total_profit_losses}")

#Average of changes, greatest increase and greatest decrease
def analyze_profit_losses(csvpath):
    changes = []
    previous_profit_loss = None
    greatest_increase = {
        "date": None,
        "amount": float("-inf")
    }
    greatest_decrease = {
        "date": None,
        "amount": float("inf")
    }

    with open(csvpath, mode='r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            current_profit_loss = float(row["Profit/Losses"])
            if previous_profit_loss is not None:
                change = current_profit_loss - previous_profit_loss
                changes.append(change)
                if change > greatest_increase["amount"]:
                    greatest_increase["amount"] = change
                    greatest_increase["date"] = row["Date"]
                if change < greatest_decrease["amount"]:
                    greatest_decrease["amount"] = change
                    greatest_decrease["date"] = row["Date"]
            previous_profit_loss = current_profit_loss

    # Calculate the average of changes
    average_change = sum(changes) / len(changes)

    return changes, average_change, greatest_increase, greatest_decrease

# Replace 'path_to_your_csv_file.csv' with the actual path to your CSV file
changes, average_change, greatest_increase, greatest_decrease = analyze_profit_losses(csvpath)

print(f"Average of changes in Profit/Losses: {average_change}")
print(f"Greatest increase in profits: {greatest_increase['date']} (${greatest_increase['amount']})")
print(f"Greatest decrease in profits: {greatest_decrease['date']} (${greatest_decrease['amount']})")

output_file_path = os.path.join("Analysis/financial_analysis.txt")
with open(output_file_path, mode='w') as file:
    file.write("Financial Analysis\n")
    file.write("------------------\n")
    file.write(f"Total Months: {total_months}\n")
    file.write(f"Total: ${total_profit_losses}\n")
    file.write(f"Average Change: ${average_change:.2f}\n")
    file.write(f"Greatest Increase in Profits: {greatest_increase['date']} (${greatest_increase['amount']})\n")
    file.write(f"Greatest Decrease in Profits: {greatest_decrease['date']} (${greatest_decrease['amount']})\n")