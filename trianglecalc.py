import math

name = input('Welcome to the triangle calculator, please enter your name ')
print('Hi ' + name)

side_a = float(input('\n' + name + ' Please enter the length of the first side: '))
side_b = float(input('Please enter the length of the second side: '))

#calculations
side_c = math.sqrt(side_a**2 + side_b**2)
side_c = round(side_c, 3)

area = 0.5*side_a*side_b
area = round(area, 3)

print('\nFor a triangle with lengths of ' + str(side_a) + ' and ' + str(side_b) + ' , the hypotenuse is ' + str(side_c))
print('The Area is ' + str(area))

