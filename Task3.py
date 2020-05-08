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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

# Define function to extract area code of the receiving side
def getReceivingAreaCode(input_list):
  if input_list[1][0] == "(":
    i = 1
    while input_list[1][i] != ")":
      i += 1
    return input_list[1][0:i+1]
  elif input_list[1][0:3] == "140":
    return "140"
  else:
    return input_list[1][0:4]

# Define function to check if the receiving area is from Bangalore
def isBangalore(some_string):
  return some_string == "(080)"

# Define function to check if the calling side is from Bangalore
def isCallingFromBangalore(input_list):
  return input_list[0][0:5] == "(080)"

# We will list all the distinct area code in this list
list_of_codes = []

# Keep track of how many calls are from Bangalore from calling and receiving side
total_call_from_Bangalore = 0
receiving_is_Bangalore = 0

# Go through calls list
# This loop has time complexity of O(n)
for line in calls:
  if isCallingFromBangalore(line):
    total_call_from_Bangalore += 1

    if len(list_of_codes) == 0:
      area_code = getReceivingAreaCode(line)
      if isBangalore(area_code):
        receiving_is_Bangalore += 1
      list_of_codes.append(area_code)
      
    else:
      area_code = getReceivingAreaCode(line)
      if isBangalore(area_code):
        receiving_is_Bangalore += 1
      if area_code not in list_of_codes:
        list_of_codes.append(area_code)

# This sorted function has time complexity of O(nlog n)
list_of_codes = sorted(list_of_codes)

# Print sorted area codes and mobile prefixes called by people in Bangalore
# Worst case time complexity is O(n)
txt = "The numbers called by people in Bangalore have codes:\n"
for code in list_of_codes:
  txt += code + "\n"
print(txt)

# Compute percentage and print result
percentage = float(receiving_is_Bangalore)/float(total_call_from_Bangalore)*100.00
txt = "{:.2f}".format(percentage) + " percent of calls from fixed lines" + \
   " in Bangalore are calls to other fixed lines in Bangalore."
print(txt)