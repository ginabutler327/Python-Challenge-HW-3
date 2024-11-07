"""PyPoll Homework Starter File."""

# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "election_analysis.txt")  # Output file path

# Initialize variables to track the election data
total = 1  # Track the total number of votes cast
votes ={}
candidate= None
pct_votes=0
Winner = None

with open(file_to_load) as election_data:
        reader = csv.reader(election_data)

        header = next(reader)

    # Loop through each row of the dataset and process it
        for row in reader:

# Define lists and dictionaries to track candidate names and vote counts
                candidate = row[2]
if candidate in votes.keys():
    votes[candidate]+=1
else:
    votes[candidate]=1
# Winning Candidate and Winning Count Tracker
print(votes)
output = f"""
Election Results
-------------------------
Total Votes:{total}
-------------------------
"""
Winner = ""
Highest_votes=0

for candidate in votes.keys():
    vote_amt=votes[candidate]
    pct_votes=round(100*vote_amt/total,3)
#if total amount of votes is greater than the total then new winner
    if vote_amt>total:
        vote_amt=total
        Winner = candidate

#output
result = f"{candidate}: {pct_votes}%({total})/n"
output +=result

winner_result = f"""-------------------------
Winner: {Winner}
-------------------------
"""
output+=winner_result

print(output)

# Print a loading indicator (for large datasets)
print(". ", end="")
