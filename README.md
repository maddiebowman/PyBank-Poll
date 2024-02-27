# PyBank-Poll

## Resources:

(I couldn't get ".." to find file) 
os.getcwd() https://www.tutorialspoint.com/python/os_getcwd.htm

help from LA breaking down txt file script (I really struggled on this part so provided my code for help breaking down script to produce txt file): 
#Open a text file for writing

for PyPoll - code returned and edited (line 50)
with open('election_results.txt', 'w') as file:
    #Write the election results to the text file
    file.write("Election Results\n")
    file.write("-------------------------\n")
    file.write(f"Total Votes: {total_votes}\n")
    file.write("-------------------------\n")
    for candidate in candidates:
        file.write(f"{candidate}: {percentages[candidate]:.3f}% ({votes[candidate]})\n")
    file.write("-------------------------\n")
    file.write(f"Winner: {winner}\n")
    file.write("-------------------------\n")

  for PyBank - code returned and edited (line 66)
output_file.write("Total Months: {}\n".format(total_months))
output_file.write("Total: {}\n".format(total))
output_file.write("Average Change: {}\n".format(average_change))
output_file.write("Greatest Increase: {}\n".format(greatest_increase))
output_file.write("Greatest Decrease: {}\n"
