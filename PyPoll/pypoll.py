import os
import csv

candidate_votes = {}
with open("Resources/election_data.csv", 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    column_names = next(csv_reader)
    for row in csv_reader:
        if row[2] in candidate_votes.keys():
            candidate_votes[row[2]] += 1 
        else: 
            candidate_votes[row[2]] = 1


election_analysis = f"""
Election Results
  -------------------------
  Total Votes: {sum(candidate_votes.values())}
  -------------------------
  Khan: 63.000% ({candidate_votes["Khan"]})
  Correy: 20.000% ({candidate_votes["Khan"]})
  Li: 14.000% ({candidate_votes["Khan"]})
  O'Tooley: 3.000% ({candidate_votes["Khan"]})
  -------------------------
  Winner: Khan
  -------------------------
"""
print(election_analysis)

with open("election_analysis.txt", 'w') as txt_file:
    txt_file.write(election_analysis)