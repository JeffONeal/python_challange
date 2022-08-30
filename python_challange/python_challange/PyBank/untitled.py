import csv

from pathlib import Path
budget_data = Path("budget_data.csv")
budget_data 

count = 0
total = 0
average = 0
minimum = 0
maximum = 0
net = 0
change_list = []
net_change = 0
total_months = 0
net_profit = 0
net_change_list = []


with open(budget_data) as file:
    reader = csv.reader(file)
    header = next(reader)
    row1 = next(reader)
    net_profit = net_profit + int(row1[1])
    previous_net = int(row1[1])
    

    for row in reader:
        total_months = total_months + 1
        count += 1
        net_profit = net_profit + int(row[1])
   
    
        # calculating monthly change average
        net_change = int(row[1]) - previous_net
        previous_net = int(row[1])
        net_change_list = net_change_list + [net_change]

        print(net_change_list)

average_net_change = sum(net_change_list)/len(net_change_list)
print(average_net_change)

max(net_change_list)

min(net_change_list)

print("--------Profit and Loss Summary---------")
print(f"Number of months: {count +1}")
print(f"Total Profit/Loss: {net_profit}")
print(f"Average Change: {average_net_change}")
print(f"Largest Profit Increase: {max(net_change_list)}")
print(f"Largest Loss Decrease: {min(net_change_list)}")


output_path = 'output.txt'

with open(output_path, 'w') as file:

    file.write(f"The total months of data was {count+1}, the total profit {net_profit}, the average change in profit and loss was {average_net_change}.  The largest profit in any month was {max(net_change_list)} and the largest loss in any month was {min(net_change_list)}")

