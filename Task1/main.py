
#homework3, Task1:PyBank
# define veriables , import data
# First import the os module
# This will allow us to create file paths across operating systems
import os
csvpath = os.path.join('PyBank', 'budget_data_1.csv')
import csv
with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    data = csv.reader(csvfile, delimiter=',')

#1 The total number of months included in the dataset
    dates, revenue, rev_change = [], [], []
    i=0
    for row in data:
        dates.append(row[0])
        revenue.append(row[1])
        i=i+1
print ('-' * 50) #separationlines
print ('-' * 50)
print ("Financial Analysis")
print ('~' * 18)
print ("Total months:",(i-1) ) #print total month


#2 The total amount of revenue gained over the entire period


revenue_total=0

for j in range (1,i) :
    val = revenue[j]
    if type(int(val)) == int :
        revenue_total = revenue_total + int(val)
    if  j > 1 :
            rev_change.append(int(revenue[j])- int(revenue[j-1]))

        

     
# 3 The greatest increase in revenue (date and amount) over the entire period

# The greatest decrease in revenue (date and amount) over the entire period
max_change = int(rev_change[0])
min_change = int(rev_change[0])
Rev_change_total = 0
for j in range (0,i-2) :
    if int(max_change) < int(rev_change[j]):
        max_change = rev_change[j]
        date1 = dates[j+2]
    if int(min_change) > int(rev_change[j]):
        min_change = rev_change[j]
        date2 = dates[j+2]
    Rev_change_total = Rev_change_total + rev_change[j]
 
# 4 The average change in revenue between months over the entire period

Average =  Rev_change_total/(i-2)

#print all results

print ("Total Revenue : ","$",revenue_total, sep='')
print ("Average Revenue Change: ","$",Average)
print ("Greatest increase in Revenue: ",date1," (",'$',max_change,")", sep='')
print ("Greatest decrease in Revenue: ",date2," (","$",min_change,")", sep='') 
print ('-' * 50) #separationlines
print ('-' * 50)



#the end


