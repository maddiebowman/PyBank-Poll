# Allows us to create file paths across operating systems
import os
# Module for reading csv files
import csv


# Specify CSV file to read
csvpath = os.path.join(os.getcwd(),"Resources", "budget_data.csv")

# Variables
net_total = 0
total_months = 0
previous_profit_loss = 1
profit_loss = 0
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999]
 # Read in CSV file 
with open(csvpath) as csvfile:

     # CSV reader specifies delimeter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=",")
 
    header = next(csvreader)

    

    # Loop through data/calculate output results
    for row in csvreader:
        total_months+=1
        net_total += int(row[1])



        if total_months == 1:
            prev = int(row[1])
        else:
            current = int(row[1]) 
            current_profit_change = current - prev
            profit_loss += current_profit_change

            if current_profit_change > greatest_increase[1]:
                greatest_increase[0] = row[0]
                greatest_increase[1] = current_profit_change
            if current_profit_change < greatest_decrease[1]:
                greatest_decrease = [row[0],current_profit_change] 

            prev = current
    

    average_change = profit_loss/(total_months - 1)

  



# Print out results
print("Financial Analysis")
print("------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})")
print(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})")

# Create text file
output_file = open("financial_analysis.txt" , "w")
              
output_file.write("Total Months: {}\n".format(total_months))
output_file.write("Total: {}\n".format(net_total))
output_file.write("Average Change: {}\n".format(average_change))
output_file.write("Greatest Increase: {}\n".format(greatest_increase))
output_file.write("Greatest Decrease: {}\n".format(greatest_decrease))

output_file.close()




