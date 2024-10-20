# PROBLEM 1 - SHOUTING

input_entries = [] # stores all user inputs.

# remains true until the length of our input_entries list is 15, inputs are stored as uppercase.
while True: 
    user_input = input()
    input_entries.append(str(user_input).upper())
    if len(input_entries) == 15:
        break

# Iterate through our input_entries list and print out each upper case entry on a new line.
for entry in input_entries:
    print(entry)
