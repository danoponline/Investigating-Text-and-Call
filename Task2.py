"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
# This is a dictionary in the form of 
# {phone1: cumulative duration, phone2: cumulative duration, ...}
cumulative_distinct_dic = {}

# For loop to go through each line in calls
for line in calls:
   
    # Only for the first line in calls
    if len(cumulative_distinct_dic) == 0:
        cumulative_distinct_dic[line[0]] = int(line[3])
        cumulative_distinct_dic[line[1]] = int(line[3])
    
    # Accumulate duration in the dictionary for each phone number (both calling and answering)
    # Create new record if doesn't exist in the dictionary
    # Checking if the key is in dictionary has worst-case time complexity of O(n)
    else:
        if line[0] not in cumulative_distinct_dic:
            cumulative_distinct_dic[line[0]] = int(line[3])
        else:
            cumulative_distinct_dic[line[0]] += int(line[3])
        if line[1] not in cumulative_distinct_dic:
            cumulative_distinct_dic[line[1]] = int(line[3])
        else:
            cumulative_distinct_dic[line[1]] += int(line[3])

# Looking for the number with the longest duration
longest_duration = None
talk_longest_phone_number = None
for phoneNumber in cumulative_distinct_dic:
    if longest_duration == None:
        longest_duration = cumulative_distinct_dic[phoneNumber]
    else:
        if cumulative_distinct_dic[phoneNumber] > longest_duration:
            longest_duration = cumulative_distinct_dic[phoneNumber]
            talk_longest_phone_number = phoneNumber

# Print result on console
txt = talk_longest_phone_number + " spent the longest time, " + format(longest_duration) + \
    " seconds, on the phone during September 2016."
print(txt)