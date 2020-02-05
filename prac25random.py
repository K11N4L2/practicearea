

class Square:
    def __init__(self, height='0', width='0'):
        self.height = height
        self.width = width
    @property
    def height(self):
        print('Retrieve height')
        return self.__height # private
    
    @height.setter
    def height(self, value):
        if value.isdigit():
            self.__height = value
        else:
            print('Please enter a number')
# add on getters and setters
# tkinter - draw out shapes
# set as module to build on shapes python drawer
