#Import modules
import os
import csv

#Set path for csv file
budgetdatapath = os.path.join('..','Resources','budgetdata.csv')

#Open file, skip header
with open (budgetdatapath,'r') as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    header = next(csvreader)
    
    #Put column values into lists
    months = []
    profitloss = []
    for row in csvreader:
        months.append(row[0])
        profitloss.append(int(row[1]))

    #Build lists for change in revenue and assign change values
    revchange = []
    maxrow =[]
    minrow = []
    for x in range(1,len(profitloss)):
        revchange.append(profitloss[x] - profitloss[x-1])
    
    #Calculate values for average, max and min changes and match max and min with the months they occurred
    avgrevchange = round(sum(revchange) / len(revchange),2)
    maxrevchange = max(revchange)
    minrevchange = min(revchange)
    maxrevchangemonth = months[(revchange.index(maxrevchange))+1]
    minrevchangemonth = months[(revchange.index(minrevchange))+1]

    #Print terminal message
    print(f"Financial Analysis\n-------------------------------\nTotal Months: {len(months)}\nTotal: ${sum(profitloss)}\nAverage Change: ${avgrevchange}\nGreatest Increse in Profits: {maxrevchangemonth} (${maxrevchange})\nGreatest Decrease in Profits: {minrevchangemonth} (${minrevchange})")

#Create path and write text file
outputfile = os.path.join(".","Output","Financial_Analysis.txt")

with open(outputfile,"w",newline="") as txt_file:
    txt_file.write(f"Financial Analysis\n-------------------------------\nTotal Months: {len(months)}\nTotal: ${sum(profitloss)}\nAverage Change: ${avgrevchange}\nGreatest Increse in Profits: {maxrevchangemonth} (${maxrevchange})\nGreatest Decrease in Profits: {minrevchangemonth} (${minrevchange})")