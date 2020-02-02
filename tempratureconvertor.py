print('Welcome to the temperature converter')

#tempi = print('choose your temp; \nC: enter 1\nF: enter 2 \nK: enter 3 ')
temp_f = float(input('\nWhat temperature in Fahrenheit would you like to convert ? '))

# if statement for option for tempi
# set measurement 
# display conversion as table

# c and k - create function add in input for different temps
temp_c = (5/9)*(temp_f - 32)
temp_k = temp_c + 273.15

temp_f = round(temp_f, 4)
temp_c = round(temp_c, 4)
temp_k = round(temp_k, 4)

# :\t for spacing 
print('\nDegrees Fahrenheit:\t' + str(temp_f))
print('Degrees Celsius:\t' + str(temp_c))
print('Degrees Kelvin:\t\t' + str(temp_k))
