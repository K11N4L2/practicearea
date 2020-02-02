print('Welcome to the Grade Sorter')

# set lit
grades = []

# get grades
grade = int(input('What is your first Grade (0 - 100)? '))
grades.append(grade)
grade = int(input('What is your second Grade (0 - 100)? '))
grades.append(grade)
grade = int(input('What is your third Grade (0 - 100)? '))
grades.append(grade)
grade = int(input('What is your fourth Grade (0 - 100)? '))
grades.append(grade)

# print out
print('\nYour Grades are: ' + str(grades))


# sort list highest to lowest
grades.sort(reverse=True)
print('Your Grades Highest to Lowest are: ' + str(grades))

# Removing the lowest two grades
print('\nThe Lowest Two Grades will now be dropped ')

# pop method lowest two gradess
removed_grade = grades.pop()
print('Removed Grade ' + str(removed_grade))
removed_grade = grades.pop()
print('Removed Grade ' + str(removed_grade))

# recap remaining grades
print('\nNice work, your highest grades are: ' + str(grades))
print('\nYour highest Grade was: ' + str(grades[0]))
