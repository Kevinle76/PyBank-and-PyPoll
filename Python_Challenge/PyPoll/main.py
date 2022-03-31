import os
import csv

No_votes = []
Candidates = []
County = []
Charles =[]
Diana =[]
Raymon =[]
Percent_of_Charles = []
Percent_of_Diana = []
Percent_of_Raymon = []

Charles_Votes = 0
Diana_Votes =0
Raymon_Votes =0

csvpath = ('D:/GT-VIRT-DATA-PT-03-2022-U-LOL/Pytho_Challenge/PyPoll/Resouces/election_data.csv')
with open(csvpath) as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")
        csvheader = next(csvreader)
              
        for row in csvreader:
            No_votes.append(row[0])
            County.append(row[1])
            Candidates.append(row[2])
            total_votes = (len(No_votes))
               
        for candidate in Candidates:
            if candidate == "Charles Casper Stockham":
                Charles.append(Candidates)
                Charles_Votes = len(Charles)
        
            elif candidate == "Diana DeGette":
                Diana.append(Candidates) 
                Diana_Votes = len(Diana) 
            
            else:
                Raymon.append(Candidates)
                Raymon_Votes = len(Raymon)
        
        Percent_of_Charles = round(((Charles_Votes/total_votes)*100),3) 
        Percent_of_Diana = round(((Diana_Votes/total_votes)*100),3)
        Percent_of_Raymon = round(((Raymon_Votes/total_votes)*100), 3)
    
        if Percent_of_Charles > max(Percent_of_Diana,Percent_of_Raymon):
            winner = "Charles Casper Stockham"  
        
        elif Percent_of_Diana > max(Percent_of_Raymon, Percent_of_Charles):
            winner = "Diana DeGette"      

        else:    
            winner = "Raymon Anthony Doane" 

        print(f'''
                Election Results
                -----------------------------
                Total Votes: {str(total_votes)}
                -----------------------------
                Charles Casper Stockham: {str(Percent_of_Charles)}% ({str(Charles_Votes)})
                Diana DeGette: {str(Percent_of_Diana)}% ({str(Diana_Votes)})
                Raymon Anthony Doane: {str(Percent_of_Raymon)}% ({str(Raymon_Votes)})
                -------------------------------- 
                Winner: {winner} 
                ''')

        f = open("Results_PyPoll.txt", "w")
        f.write(f'''
                Election Results
                ----------------------------
                Total Votes: {total_votes}
                ----------------------------
                Charles Casper Stockham:  {str(Percent_of_Charles)}% ({str(Charles_Votes)})
                Diana DeGette: {str(Percent_of_Diana)}% ({str(Diana_Votes)})
                Raymon Anthony Doane:  {str(Percent_of_Raymon)}% ({str(Raymon_Votes)})
                ----------------------------
                Winer is {winner}
                ----------------------------
                ''')    
        f.close()
