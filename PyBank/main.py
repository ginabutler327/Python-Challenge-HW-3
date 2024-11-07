
# Dependencies
import csv
import os
# Files to load and output (update with correct file paths)
filepath = os.path.join("Resources1", "budget_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path

# Define variables to track the financial data
total_months = 0
total_net = 0
# Add more variables to track other necessary financial data
average_change = 0
greatest_increase = 0
greatest_decrease = 0
last_month_profit = 0
current_month_profit = 0
total_change = 0
max_month=None
min_month=None
# Open and read the csv
with open(filepath) as financial_data:
    reader = csv.reader(financial_data)

    # Skip the header row
    header = next(reader)

    # Extract first row to avoid appending to net_change_list
def extract_first_row(data):
    if not data:
        return None, []
    first_row = data [0]
    remaining_data = data[1:]

    # Track the total and net change


    # Process each row of data
    for row in csv.reader(financial_data):
# Define variables to track the financial data
        total_months += 1    
        total_net += int(row[1])
        #check if first row - skip first row
        if total_months == 1:
            last_month_profit = int(row[1])
        else:
            #get change
            current_month_profit = int(row[1])
            change = current_month_profit - last_month_profit
            total_change += change
        
        # Track the total
        total_net = sum(total_change)

        # Track the net change


        # Calculate the greatest increase in profits (month and amount)
    if greatest_increase == max(total_change):
    # Find the index of the greatest increase
        index_of_greatest_increase = total_change.index(greatest_increase)

# Get the corresponding date

        date_of_greatest_increase = dates[index_of_greatest_increase]

def display_greatest_increase(date, increase):
    print(f"Date: {date}, Greatest Increase: {increase}")


        # Calculate the greatest decrease in losses (month and amount)
    if greatest_decrease == min(total_change):
   # Find the index of the greatest increase
        index_of_greatest_decrease = total_change.index(greatest_decrease)

# Get the corresponding date

        date_of_greatest_decrease = dates[index_of_greatest_decrease]

def display_greatest_decrease(date, decrease):
    print(f"Date: {date}, Greatest Decrease: {decrease}")


# Calculate the average net change across the months
average_change = total_change/(total_months - 1)

# Print the output

print(f"reader:{financial_data}")
output = f""" 

Financial Analysis
----------------------------
Total Months: {total_months}
Total: ${total_net}
Average Change: ${round(average_change,2)}
Greatest Increase in Profits: {max_month} (${greatest_increase})
Greatest Decrease in Profits: {min_month} (${greatest_decrease})
"""
print(output)
# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)
