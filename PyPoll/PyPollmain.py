import csv
from collections import defaultdict
from pathlib import Path


# Read CSV file
input_file = Path("Resources/election_data.csv")
output_file = Path("election_results.txt")

total_votes = 0
candidates = {}
 



with input_file.open() as csv_file:
    reader = csv.reader(csv_file)
    next(reader) 

for row in reader:
        candidate = row[2]
        total_votes += 1
        candidates[candidate] += 1
# Calculate Votes and Pinpoint Winner
winning_candidate = {"name": "", "votes": 0}
total_candidates = []


for candidate, votes in candidates.items():
    percentage = (votes / total_votes) * 100
    total_candidates.append(f"{candidate}: {percentage:.3f}% ({votes})")

    if votes > winning_candidate["votes"]:
        winning_candidate["name"] = candidate
        winning_candidate["votes"] = votes    
        

report = f"""Election Results
-------------------------
Total Votes: {total_votes}
-------------------------
Candidates: {', '.join(total_candidates)}
-------------------------
Winner: {winning_candidate["name"]}
-------------------------
"""

# Print to Terminal Box
print(report)

#Spit Out to Text File
with open("Analysis/election_results.txt", "w") as txtfile:
    txtfile.write(report)
