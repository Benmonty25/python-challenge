import os

import csv

row_count = 0
monthcount = 0
totaldifference = 0
bestmonthdate = 0
worstmonthdate = 0

csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath) as csvfile:
    csvreader =csv.reader(csvfile, delimiter=',')

    next(csvreader, None) 

    datecount=[]
    profitloss = []
    differencecolumn = []
    linechanges=[]

    for row in csvreader:
        datecount.append(row[0])
        profitloss.append(row[1])
    
    for month in datecount:
        monthcount += 1   
    
    for row in profitloss:
        row_count += int(row)

    for i in range(0,len(profitloss)-1):
        linechanges = int(profitloss[i+1]) - int(profitloss[i])

        differencecolumn.append(linechanges)
      
    for row in differencecolumn:
        totaldifference += int(row)

    Average = round(totaldifference / (monthcount-1), 2)

    bestmonth = round(max(differencecolumn),0)

    worstmonth = round(min(differencecolumn),0)

    for i in range(0,len(differencecolumn)):
        if differencecolumn[i] == bestmonth:
            bestmonthdate = str(datecount[i+1])

        if differencecolumn[i] == worstmonth:
            worstmonthdate = str(datecount[i+1])
        
def output():
    return (f"Financial Analysis\n----------------------\nTotal Months: {monthcount}\nTotal: ${row_count}\nAverage Change: ${Average}\nGreatest Increase in Profits: {bestmonthdate} (${bestmonth})\nGreatest Decrease in Profits: {worstmonthdate} (${worstmonth})")

print(output())

textpath = os.path.join('analysis', 'analysis.txt')
with open(textpath, 'w') as textfile:
    textfile.write(str(output()))
