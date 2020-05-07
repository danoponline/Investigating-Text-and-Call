"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
#This list is for collecting distinct phone numbers in all the records
number_distinct_list =[]

#For loop to go through each line in texts
for index in range(len(texts)):
    if len(number_distinct_list) == 0:
        number_distinct_list.append(texts[index][0])
    else:
        #Hidden loop here to go through each element in number_distinct_list
        #Worst case can be the same length as the number of line in texts
        if texts[index][0] not in number_distinct_list:
            number_distinct_list.append(texts[index][0])
    
    #Another hidden nested loop here
    if texts[index][1] not in number_distinct_list:
        number_distinct_list.append(texts[index][1])

#For loop to go through each line in calls
for index in range(len(calls)):
    if len(number_distinct_list) == 0:
        number_distinct_list.append(calls[index][0])
    else:
        #Hidden nested loop here to go through each element in number_distinct_list
        #Worst case can be the same length as the number of line in calls
        if calls[index][0] not in number_distinct_list:
            number_distinct_list.append(calls[index][0])
    
    #Another hidden nested loop here
    if calls[index][1] not in number_distinct_list:
        number_distinct_list.append(calls[index][1])

count = len(number_distinct_list)
print("There are " + format(count) + " different telephone numbers in the records.")