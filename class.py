# class Sample:
#     pass
# my_sample = Sample()
# print(type(my_sample))

class Dog():
    def __init__(self,category,name,spots):
        self.category = category
        self.name = name
        self.spots= spots
my_list = Dog(category='dog',name='kuper',spots='YES')
print(my_list.category)
print(my_list.name)
print(my_list.spots)

