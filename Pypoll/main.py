#PyPoll.py

#Create file
import os
import csv

#set file path
file_path= os.path.join ('.', 'Resources','election_data.csv')

#declare all variables
Stockham_ballot = 0
DeGette_ballot = 0
Doane_ballot = 0
total_ballot = 0

#open csv file
with open(file_path,newline="", encoding="utf-8") as electionresult:
    csvreader = csv.reader(electionresult, delimiter=',')


    #skip header
    header = next(csvreader)

    #count ballot ID
    for row in csvreader:
        total_ballot +=1

        if row[2] =="Charles Casper Stockham":
            Stockham_ballot +=1
        elif row [2] == "Diana DeGette":
            DeGette_ballot +=1
        elif row [2] == "Raymon Anthony Doane":
            Doane_ballot +=1

#Create a dictionary to find the winner
all_candidates = ["Charles Casper Stockham", "Diana DeGette", "Raymon Anthony Doane"]
candidate_votes = [Stockham_ballot, DeGette_ballot, Doane_ballot]

#Zip all_candidates and total_votes 
dict_all_candidates_and_candidate_votes = dict(zip(all_candidates,candidate_votes))
key = max(dict_all_candidates_and_candidate_votes, key=dict_all_candidates_and_candidate_votes.get)

#print outcome summary for percentage


Stockham_outcome = (Stockham_ballot/total_ballot)*100
DeGette_outcome = (DeGette_ballot/total_ballot)*100
Doane_outcome = (Doane_ballot/total_ballot)*100

#print the summary analysis
print ("Election Results")
print ("-------------------------")
print (f"Total Votes: {total_ballot}")
print ("-------------------------")
print (f"Charles Casper Stockham: {Stockham_outcome:.3f}% ({Stockham_ballot})")
print (f"Diana DeGette: {DeGette_outcome:.3f}% ({DeGette_ballot})")
print (f"Raymon Anthony Doane: {Doane_outcome:.3f}% ({Doane_ballot})")
print ("-------------------------")
print (f"Winner: {key}")
print ("-------------------------")

#summary output file
summary_output = os.path.join ('.', 'Election Results')
with open (summary_output, "w") as file:

    file.write(f"Election Results")
    file.write("\n")
    file.write(f"----------------------------")
    file.write("\n")
    file.write(f"Total Votes: {total_ballot}")
    file.write("\n")
    file.write(f"----------------------------")
    file.write("\n")
    file.write(f"Charles Casper Stockham: {Stockham_outcome:.3f}% ({Stockham_ballot})")
    file.write("\n")
    file.write(f"Diana DeGette: {DeGette_outcome:.3f}% ({DeGette_ballot})")
    file.write("\n")
    file.write(f"Raymon Anthony Doane: {Doane_outcome:.3f}% ({Doane_ballot})")
    file.write("\n")
    file.write(f"----------------------------")
    file.write("\n")
    file.write(f"Winner: {key}")
    file.write("\n")
    file.write(f"----------------------------")

