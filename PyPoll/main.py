import os
import csv

# Path to CSV file
election_csv = os.path.join(os.getcwd(), "Resources", "election_data.csv")

# Variables
total_votes = 0
candidates = {}
winner = ""
winner_votes = 0

# Read in CSV file
with open(election_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
  
    next(csvreader)
    # Loop through each row in CSV file
    for row in csvreader:
        # Total votes counter
        total_votes += 1
        # Find candidate name in data set (row 2)
        candidate_name = row[2]
        # If candidate is already in dictionary, increase vote count by 1
        if candidate_name in candidates:
            candidates[candidate_name] += 1
        # If candidate is not already in dictionary, add name and set vote count to 1
        else:
            candidates[candidate_name] = 1

# Print Election Results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")

# Calculate and print percentage of votes for each candidate and total votes
for candidate, votes in candidates.items():
    percentage = (votes / total_votes) * 100
    print(f"{candidate}: {percentage:.3f}% ({votes})")
    # Determine winner
    if votes > winner_votes:
        winner = candidate
        winner_votes = votes

print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

# Open a text file for writing
with open('election_results.txt', 'w') as file:
    # Print election results to text file
    file.write("Election Results\n")
    file.write("-------------------------\n")
    file.write(f"Total Votes: {total_votes}\n")
    file.write("-------------------------\n")
    for candidate in candidates:
        percentage = (votes / total_votes) * 100
        file.write(f"{candidate}: {percentage:.3f}% ({votes})\n")
    file.write("-------------------------\n")
    file.write(f"Winner: {winner}\n")
    file.write("-------------------------\n")

# Print message indicating results have been saved to a file
print("Election results have been saved to election_results.txt.")