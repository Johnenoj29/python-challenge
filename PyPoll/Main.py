import os
import csv
from random import vonmisesvariate

#-----------------------------------------------------
# Set working directory to where this Python file is
os.chdir(os.path.dirname(__file__))

election_data_csv = os.path.join("Resources", "election_data.csv")
output = os.path.join("analysis", "election_analysis.txt")

#define variables and lists
count = 0
candidate_list = []
individual_candidate = []
vote_per_candidate = []
percentage_vote = []


# Open and read csv
with open(election_data_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

# Read through each row of data after the header
    csv_header = next(csv_reader )
    for row in csv_reader:

    # count total votes
        count += 1
    # set candidate names in data set to candidate_list
        candidate_list.append(row[2])

    # create set for indidivual candidate assigned to total votes and percentage
    for x in set (candidate_list):
        individual_candidate.append(x)
        y = candidate_list.count(x)
        vote_per_candidate.append(y)

        p = (y/count)*100
        percentage_vote.append(p)

    # calculate winner
    winning_vote = max (vote_per_candidate)
    winner = individual_candidate[vote_per_candidate.index(winning_vote)]

#Print and create output file

output_file=(f"Election Results\n"
f"----------------------------\n"
f"Total Votes: {count}\n"
f"----------------------------\n"
f"{individual_candidate}: {percentage_vote}% {vote_per_candidate} \n"
f"----------------------------\n"
f"Winner: {winner}\n")

print(output_file)

with open(output, "w") as output_txt:
    output_txt.write(output_file)
