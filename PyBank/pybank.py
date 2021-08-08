import os
import csv

row = []
with open("Resources/budget_data.csv", 'r') as file_handler:
    print(file_handler)
    csv_reader = csv.reader(file_handler, delimiter=",")
    head = next(csv_reader)
    print(head)
    first_row =  next(csv_reader)
    print(first_row)
    change = []
    sum = int(first_row[1])
    row_count = 1
    prev_change = int(first_row[1])
    net_change = 0
    max_change = 0
    min_change = 0
    max_change_month = ""
    min_change_month = ""
    for row in csv_reader:
        row_count += 1
        row[1] = int(row[1])
        sum += row[1] 
        net_change = row[1]-prev_change
        change.append(net_change)
        prev_change = row[1]
        prev_net = int(row[1])
        net_change = int(row[1]) - prev_net
       
        max_change_month = max_change_month + row[0]
        if (net_change > max_change):
            max_change= row[1]
            max_change = prev_net
           
            min_change_month = min_change_month + row[0]   
            if (net_change < min_change):
                min_change = row[1]
                min_change = prev_net

#net_monthly_avg = sum(net_change_list) / len(net_change_list)
            
       
    
chng = 0
for x in change:
    chng += x
# print(chng, len(change))
ret = f"""
Financial Analysis
  ----------------------------
  Total Months: {row_count}
  Total: ${sum}
  Average  Change: ${(chng/len(change))}
  Greatest Increase in Profits: {max_change_month} (${max_change})
  Greatest Decrease in Profits: {min_change_month} (${min_change})
"""
print(ret)

       
   with open("budget_data.txt", 'w') as txt_file:
    txt_file.write(ret)

