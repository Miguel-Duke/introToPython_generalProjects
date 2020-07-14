# Week 3 assigned project.
# Start the project with two empty lists, one for grades and one for students.
# Allow the user to enter 5 student names, prompted for each name one at a time.
# These names are to be placed in the appropriate list.
# Allow the user to enter final grades, prompted for each grade one at a time.
# These grades are to be placed in the appropriate list.
#
# Calculate and print out the average of all grades.
# Print out a students name and their grades.
# Print out the two highest grades.
# Print out the two lowest grades.
#
# Be sure that the program has well defined comments.
# Also be sure that all values output have descriptive wording.

# First we establish variables for the lists.
student_roster = []
student_grades= []

# Next we prompt the user to populate the lists with students and grades.
student_0 = input('Please enter a student\'s name:')
student_0_grade = int(input('Please enter their grade:'))

student_1 = input('Please enter a student\'s name:')
student_1_grade = int(input('Please enter their grade:'))

student_2 = input('Please enter a student\'s name:')
student_2_grade = int(input('Please enter their grade:'))

student_3 = input('Please enter a student\'s name:')
student_3_grade = int(input('Please enter their grade:'))

student_4 = input('Please enter a student\'s name:')
student_4_grade = int(input('Please enter their grade:'))

# Now we take the information provided by the user and add each element to
# the appropriate list.
student_roster.append(student_0)
student_roster.append(student_1)
student_roster.append(student_2)
student_roster.append(student_3)
student_roster.append(student_4)

student_grades.append(student_0_grade)
student_grades.append(student_1_grade)
student_grades.append(student_2_grade)
student_grades.append(student_3_grade)
student_grades.append(student_4_grade)

# Here we calculate the average grade of the collective students and set this
# information to the variable 'avg_grades'.
avg_grades = int((student_grades[0]) + (student_grades[1]) + (student_grades[2]) + (student_grades[3]) + (student_grades[4]))
avg_grades = avg_grades / len(student_grades)
print('\nThe average grade of this german class is:', avg_grades)

# We now generate a list showing each student with their grade beside their name.
print('\nBelow is a table displaying each student and their grade')
print(student_0, student_0_grade)
print(student_1, student_1_grade)
print(student_2, student_2_grade)
print(student_3, student_3_grade)
print(student_4, student_4_grade)

# At this point we find the two highest grades in the class and print them
# for the end user to view.
copy_student_grades = student_grades # Copying the list so we can remove elements.
highestGrade = max(copy_student_grades)
copy_student_grades.remove(highestGrade)
secondHighest = max(copy_student_grades)
print('\nThe highest grade is:', highestGrade)
print('The second highest grade is:', secondHighest)

# Finally we will find the two lowest grades in the class and print them
# for the end user to view.
lowestGrade = min(copy_student_grades)
copy_student_grades.remove(lowestGrade)
secondLowest = min(copy_student_grades)
print('\nThe lowest grade is:', lowestGrade)
print('The second lowest grade is:', secondLowest)


