# enter list 
# define data type / organise print lists / reverse order set input to choose

# define lists
num_strings = ['15', '100', '42', '55']
num_ints = [15, 100, 42, 55]
num_floats = [2.2, 5.0, 1.245, 0.142857]
num_lists = [[1,2,3], [4,5,6], [7,8,9]]

# Summary of Lists
print('\t\tSummary Table')

print('\nThe Variable num_strings is a ' + str(type(num_strings)) + '.')
print('\nIt contains the elements: ' + str(num_strings))
print('\nThe Element ' + num_strings[0] + ' is a ' + str(type(num_strings[0])))

print('\nThe Variable num_strings is a ' + str(type(num_ints)) + '.')
print('\nIt contains the elements: ' + str(num_ints))
print('\nThe Element ' + str(num_ints[0]) + ' is a ' + str(type(num_ints[0])))

print('\nThe Variable num_strings is a ' + str(type(num_floats)) + '.')
print('\nIt contains the elements: ' + str(num_strings))
print('\nThe Element ' + str(num_floats[0]) + ' is a ' + str(type(num_floats[0])))

print('\nThe Variable num_strings is a ' + str(type(num_lists)) + '.')
print('\nIt contains the elements: ' + str(num_strings))
print('\nThe Element ' + str(num_lists[0]) + ' is a ' + str(type(num_lists[0])))

num_strings.sort()
num_ints.sort()

print('\nNow sorting num_strings and num_ints...')
print('\nSorted num_strings ' + str(num_strings))
print('\nSorted num_ints ' + str(num_ints))




# scf 
