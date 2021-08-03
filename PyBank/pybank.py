import os
import csv

total_votes = 0 
with open("Resources/budget_data.csv", 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    for row in csv_reader:
        
