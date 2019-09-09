#Import modules
import os
import csv

#Set path for csv file
electiondatapath = os.path.join('..','Resources','election_data.txt')

#Open file, skip header
with open (electiondatapath,'r') as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    header = next(csvreader)
    
    #makelist of candidates and count for total votes
    candidates = [row[2] for row in csvreader]
    totalvotes = len(candidates)
    winner = max(set(candidates), key=candidates.count)

    #Build dictionary of candidates as keys and votes as values
    votespercan = {}
    for can in candidates:
        if not votespercan.get(can):
            votespercan[can] = 1
        else:
            votespercan[can] += 1
            
    #Print Terminal Message
    print("Election Results")
    print("------------")
    print(f"Total Votes: {totalvotes}")
    print("------------")
    for k,v in votespercan.items():
        print(f"{k}: {round(((v/totalvotes)*100),3)}% {v}")
    print("------------")
    print(f"Winner: {winner}")
    print("------------")

#Create path and write text file
outputfile = os.path.join("Output","electionresults.txt")

with open(outputfile,"w",newline="\n") as txt_file:
    txt_file.write("Election Results\n")
    txt_file.write("------------\n")
    txt_file.write(f"Total Votes: {totalvotes}\n")
    txt_file.write("------------\n")
    for i, (k,v) in enumerate(votespercan.items()):
        txt_file.write(f"{k}: {round(((v/totalvotes)*100),3)}% {v}\n")
    txt_file.write("------------\n")
    txt_file.write(f"Winner: {winner}\n")
    txt_file.write("------------\n")
