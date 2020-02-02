# welcome
print('Welcome to the counter')

# get input
name = input('\nHi, please enter your name..').title().strip()
print('Hello, ' + name)

# set message and letter
print('I will count the number of times a specific letter occurs in a message')
message = input('\nPlease enter a message')
letter = input('Which letter would you like to count?')

# count capital and lowercase letters
message = message.lower()
letter = letter.lower()

letter_count = message.count(letter)
print('\n' + name + ' your message has ' + str(letter_count) + ' Occurences of the letter ' + letter)