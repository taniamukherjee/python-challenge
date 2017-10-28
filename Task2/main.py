
#homework3, Task2:PyPoll
# define veriables , import data
# First import the os module
# This will allow us to create file paths across operating systems
import os
csvpath = os.path.join('PyPoll', 'election_data_2.csv')
import csv
with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    data = csv.reader(csvfile, delimiter=',')

#1 The total number of votes cast
    voter_id, county, candidate, candidate_total,candidate_percent = [], [], [], [], []
 
    i=0
    for row in data:
        if len(row[1]) != 0 :
            voter_id.append(row[0])
            candidate.append(row[2])
            i=i+1
    print ("vote count",(i-1) ) #print total vote
    total_vote = i-1
    #print (total_vote)
#2 A complete list of candidates who received votes  
    election_candidate = set(candidate[1:])
    election_candidate_list = list(election_candidate)

    #print (election_candidate_list)
     
#3 The percentage of votes each candidate won


    for j in range (0,len(election_candidate_list)) :
        candidate_total.append(0)
        for i in range (1, len(candidate)) :
            if   candidate[i] == election_candidate_list[j] :
                candidate_total[j] = candidate_total[j] + 1 
        candidate_percent.append(100*(candidate_total[j]/total_vote))
        #print (candidate_percent[j])
       
    for j in range (0,3) :
        print (election_candidate_list[j],":", candidate_percent[j],"%","(",candidate_total[j],")")
#4 The winner of the election based on popular vote.

           
w_max = candidate_total[0]
max_pos = 0
for i in range(0,3) :

    if  w_max <candidate_total[i] :
           max_pos = i
           winner = election_candidate_list[max_pos] 
           print ("winner is", winner)



#the end
