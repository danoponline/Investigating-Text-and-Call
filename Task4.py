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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

# Create a list of phone number that is not telemarketing by appending all the distinct number
# from texts list and receiving number in calls list
# Worst-case time complexity is O(n^2)

# Comments from mentor: instead of checking first before appending:
# you could append to the list first(complexity: O(1))
# after the loop is over, you can change the list to a set( complexity: 0(n))
# This should reduce the time complexity to O(n)

def creatNotTeleMarketList(texts_list,calls_list):
    not_telemarket_list = []
    
    # Loop in texts_list
    # Worst-case time complexity of this loop is O(n^2)
    for line in texts_list:
        if len(not_telemarket_list) == 0:
            not_telemarket_list.append(line[0])
            not_telemarket_list.append(line[1])
        else:
            if line[0] not in not_telemarket_list:
                not_telemarket_list.append(line[0])
            if line[1] not in not_telemarket_list:
                not_telemarket_list.append(line[1])
    
    # Loop in calls_list
    # Worst-case time complexity of this loop is O(n^2)
    for line in calls_list:
        if len(not_telemarket_list) == 0:
            not_telemarket_list.append(line[1])
        else:
            if line[1] not in not_telemarket_list:
                not_telemarket_list.append(line[1])

    return not_telemarket_list

# Start of main program
# This is a list that will capture potential telemarketing
potential_telemarket_list = []

# Call function to create not telemarket list
# Worst-case time complexity is O(n^2)
not_telemarket_list = creatNotTeleMarketList(texts,calls)

# Loop in calls list
# Worst-case time complexity of this loop is O(n^3)

# Comment from mentor: instead of checking first before appending:
# you could append to the list first(complexity: O(1))
# after the loop is over, you can change the list to a set( complexity: 0(n))
# This should reduce time complexity to O(n^2)

for line in calls:
    if line[0] not in not_telemarket_list:
        if len(potential_telemarket_list) == 0:
            potential_telemarket_list.append(line[0])
        else:
            if line[0] not in potential_telemarket_list:
                potential_telemarket_list.append(line[0])

# Sort this list. Worst-case time complexity is O(n log n)
potential_telemarket_list = sorted(potential_telemarket_list)

# Printing potential telemarket
# Worst-case Time complexity is O(n)
txt = "These numbers could be telemarketers: \n"
for number in sorted(potential_telemarket_list):
    txt += number + "\n"
print(txt)
# Comment from mentor: this print can be simplified to
# print("These numbers could be telemarketers:",*potential_telemarket_list,sep="\n")


