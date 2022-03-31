import os
import csv

Months=[]
PL=[]
PL_change=[]
total_months = 0

csvpath = ('D:/GT-VIRT-DATA-PT-03-2022-U-LOL/Pytho_Challenge/PyBank/Resources/budget_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csvheader = next(csvreader)
   
    for row in csvreader:
        Months.append(row[0])
        PL.append(int(row[1]))
                      
    for x in range(1,len(PL)):
        PL_change.append(int(PL[x]) - int(PL[x-1]))
        Average_PL_change = round(sum(PL_change)/len(PL_change),2)
      
        total_months= len(Months)
        greatest_increase = max(PL_change)
        greatest_decrease = min(PL_change)

    print(f'''
        Financial Analysis Summary:
        ---------------------------
        Total Months: {str(total_months)}
        Total: ${str(sum(PL))}
        Average Change: ${str(Average_PL_change)}
        Greatest Increase in Profits: ${str(greatest_increase)} on ({str(Months[PL_change.index(greatest_increase)+1])})
        Greatest Decrease in Profits: ${str(greatest_decrease)} on ({str(Months[PL_change.index(greatest_decrease)+1])})
        ''')

    f = open("results_PyBank.txt", "w")
    f.write(f'''
            Financial Analysis Summary:
            ---------------------------
            Total Months: {str(total_months)}
            Total: ${str(sum(PL))}
            Average Change: ${str(Average_PL_change)}
            Greatest Increase in Profits: ${str(greatest_increase)} on ({str(Months[PL_change.index(greatest_increase)+1])})
            Greatest Decrease in Profits: ${str(greatest_decrease)} on ({str(Months[PL_change.index(greatest_decrease)+1])})
            ''')
    f.close()


