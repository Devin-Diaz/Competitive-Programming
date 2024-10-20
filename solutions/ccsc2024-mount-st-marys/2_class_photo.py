# PROBELM 2 - Class Photo

all_student_heights = [] # will store sublists of student heights. Each sublist denoting a class of students.

# this function is responsible for retrieving sublists of student heights until -1 is entered indicating end of inputs.
while True:
    user_input = input()
    if user_input == '-1': break
    student_height_sublist = user_input.split(' ') # converting to array format.
    student_height_sublist = [int(height) for height in student_height_sublist] # casting string entries to integer type.
    all_student_heights.append(student_height_sublist)

# boolean function that checks if student heights are in ascending order
def in_ascending_order(student_height_sublist):
    for i in range(len(student_height_sublist) - 1):
        if student_height_sublist[i] > student_height_sublist[i + 1]: # first number is greater than second, we reach a contradiction.
            return False
    return True

# boolean function that checks if student heights are in descending order
def in_descending_order(student_height_sublist):
    for i in range(len(student_height_sublist) - 1):
        if student_height_sublist[i] < student_height_sublist[i + 1]: # first number is less than second, we reach a contradiction.
            return False
    return True

# iterate through sublists, if sublist is in ascending OR descending, print yes, otherwise print no.
for student_height_sublist in all_student_heights:
    if in_ascending_order(student_height_sublist):
        print('yes')
    elif in_descending_order(student_height_sublist):
        print('yes')
    else:
        print('no')
