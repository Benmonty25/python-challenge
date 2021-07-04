import os

import csv

votercount = 0
votes = 0
percentage = 0
totalvotes = 0

csvpath = os.path.join('Resources', 'election_data.csv')

with open(csvpath) as csvfile:
    csvreader =csv.reader(csvfile, delimiter=',')

    next(csvreader, None) 

    voterid=[]
    county = []
    candidate = []

    for row in csvreader:
        voterid.append(row[0])
        county.append(row[1])
        candidate.append(row[2])

    for row in voterid:
        votercount += 1

    khanvotes = 0
    correyvotes = 0
    livotes = 0
    otooleyvotes = 0

    for i in range(0,len(candidate)):
        if candidate[i] == "Khan":
            khanvotes += 1
            khanpercent = format(khanvotes / votercount *100,".3f")
        
        if candidate[i] == "Correy":
            correyvotes += 1
            correypercent = format(correyvotes / votercount *100,".3f")
        
        if candidate[i] == "Li":
            livotes += 1
            lipercent = format(livotes / votercount *100,".3f")
        
        if candidate[i] == "O'Tooley":
            otooleyvotes += 1
            otooleypercent = format(otooleyvotes / votercount *100,".3f")

    candidatevotes = [["Khan",khanvotes],["Correy",correyvotes],["Li",livotes],["O'Tooley",otooleyvotes]]
    
    candidatefinal = []
    votetotal = []

    for row in candidatevotes:
        candidatefinal.append(row[0])
        votetotal.append(row[1])
    
    topcandidate = max(votetotal)
   
    winner = 0
   
    for i in range(0,len(votetotal)):
        if votetotal[i] == topcandidate:
            winner = candidatefinal[i]


def output():
    return (f"Election Results\n---------------------------\nTotal Votes: {votercount}\n---------------------------\nKhan: {khanpercent}% ({khanvotes})\nCorrey: {correypercent}% ({correyvotes})\nLi: {lipercent}% ({livotes})\nO'Tooley: {otooleypercent}% ({otooleyvotes})\n---------------------------\nWinner: {winner}\n---------------------------")

print(output())

textpath = os.path.join('analysis', 'analysis.txt')
with open(textpath, 'w') as textfile:
    textfile.write(str(output()))