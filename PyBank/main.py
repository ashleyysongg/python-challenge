#create file
import os
import csv

#set file path
filepath = os.path.join ('.','Resources','budget_data.csv')

#create list to store the data
all_months = []
all_profit = []
monthly_change = []

#open csv file
with open(filepath, newline="", encoding = "utf-8") as pybank:
   csvreader = csv.reader(pybank, delimiter=",")
   #make sure to skip headers
   header = next(csvreader)

#Store data into a dictionary
   for row in csvreader:
       all_months.append(row[0])
       all_profit.append(int(row[1]))

#calculate monthly change
   for i in range(len(all_profit)-1):
       
       #calculate monthly change
       monthly_change.append(all_profit[i+1]-all_profit[i])

#Calculate max and min of monthly profit change
maximum_increase = max(monthly_change)
maximum_decrease = min(monthly_change)

maximum_increase_month = monthly_change.index(max(monthly_change)) +1
maximum_decrease_month = monthly_change.index(min(monthly_change)) +1


#Print
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(all_months)}")
print(f"Total: ${sum(all_profit)}")
print(f"Average Change: ${round(sum(monthly_change)/len(monthly_change),2)}")
print(f"Greatest Increase in Profits: {all_months[maximum_increase_month]} (${(str(maximum_increase))})")
print(f"Greatest Decrease in Profits: {all_months[maximum_decrease_month]} (${(str(maximum_decrease))})")

#create file to export
summary = os.path.join ('.', 'Financial_Analysis_Summary.txt')

with open(summary, "w") as file:
    
#print summary
    file.write("Financial Analysis")
    file.write("\n")
    file.write("----------------------------")
    file.write("\n")
    file.write(f"Total Months: {len(all_months)}")
    file.write("\n")
    file.write(f"Total: ${sum(all_profit)}")
    file.write("\n")
    file.write(f"Average Change: ${round(sum(monthly_change)/len(monthly_change),2)}")
    file.write("\n")
    file.write(f"Greatest Increase in Profits: {all_months[maximum_increase_month]} (${(str(maximum_increase))})")
    file.write("\n")
    file.write(f"Greatest Decrease in Profits: {all_months[maximum_decrease_month]} (${(str(maximum_decrease))})")
