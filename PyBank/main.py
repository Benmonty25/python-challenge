import os

import csv
from typing import Counter

row_count = 0

csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath) as csvfile:
    csvreader =csv.reader(csvfile, delimiter=',')

    next(csvreader, None) 

    datecount=[]
    profitloss = []
    differencecolumn = []

    for row in csvreader:
        datecount.append(row[0])
        profitloss.append(row[1])
    
    monthcount = 0
    for month in datecount:
        monthcount += 1   
    
    for row in profitloss:
        row_count += float(row)

    linechanges=[]

    for i in range(0,len(profitloss)-1):
        linechanges = float(profitloss[i+1]) - float(profitloss[i])

        differencecolumn.append(linechanges)

    totaldifference = 0
    
    for row in differencecolumn:
        totaldifference += float(row)

    Average = round(totaldifference / (monthcount-1), 2)

    bestmonth = max(differencecolumn)

    worstmonth = min(differencecolumn)

    print(bestmonth)
    print(worstmonth)

    bestmonthdate = datecount.index(differencecolumn,bestmonth)
    print(bestmonthdate)
    
    # bestmonthdate = 0
    # bestmonthnumber = 0
    # worstmonthdate = 0
    # worstmonthnumber = 0

    # for i in range(0,len(differencecolumn)):
    #     bestmonth = 0
    #     if differencecolumn[i] > bestmonth:
    #         bestmonth = float(differencecolumn[i])
    #         bestmonthdate = datecount[i]
            
    #     worstmonth = 0
    #     if differencecolumn[i] < worstmonth:
    #         worstmonth = float(differencecolumn[i])
    #         worstmonthdate = str(datecount[i])
        

#     print(f"Financial Analysis")
#     print("-"*20)
#     print(f"Total Months: {monthcount}")
#     print(f"Total: ${row_count}")
#     print(f"Average Change: ${Average}")
#     print(f"Greatest Increase in Profits: {bestmonthdate} ({bestmonth})")
#     print(f"Greatest Decrease in Profits: {worstmonthdate} ({worstmonth})") 
# #         print(row)


