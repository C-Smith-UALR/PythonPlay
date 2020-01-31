class Polygon:
    def __init__(self, **kwargs):
        if 'width' in kwargs:
            self.width = kwargs['width']
        else:
            self.width = 0

        if 'height' in kwargs:
            self.height = kwargs['height']
        else:
            self.height = 0



#set these to whatever are the 'sane zero values' for number this is zero
#for string this is empty string


class Triangle(Polygon):
    def __init__(self, **kwargs):
        if 'name' in kwargs:
            self.name = kwargs['name']
        else:
            self.name = ''
        kwargs['num_sides'] = 3
        super(Triangle, self).__init__(**kwargs)


    def __str__(self):
        return_string = 'My Name is: %s\n' % self.name
        return_string += 'My width is: %d' % self.width
        return return_string

    def get_area(self):
        return (self.width * self.height) / 2.0


my_triangle = Triangle(name='Triangle!', width=6, height=7)
print(my_triangle)
#print('My triangle\'s area is: %f' % my_triangle.get_area())
