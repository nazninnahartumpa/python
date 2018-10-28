# loc = 'Bank'
# if loc =='shop':
#     print('I know the place')
# elif loc == 'Bank':
#     print('Yes it is')
# else:
#     print('I do not know the place')

# # for loop exercise
# my_list = [1,2,3,4,5,6,7,8,9,10]
# for num in my_list:
#     if num % 2 == 0:
#         print(num)
#     else:
#         print(f'Odd Number:{num}')
# #another exercise
# for letter in 'hello world':
#     print(letter)

# #tuple in list
# my_list2 = [(1,2),(3,4),(4,5)]
# for a,b in my_list2:
#     print(b)

#for loop in dictionary
# d = {'k1':1,'k2':2,'k3':4}

# for value in d.keys():
#     print(value)

# x = 1
# while x < 11:
#     print(f'the number is {x}')
#     x += 1
# else:
#     print('none')

# for num in range(0,11,2):
#     print(num)
#zip function converts list to tuple
# list1 = [1,2,3,4]
# list2 = [5,6,7]
# for item in zip(list1,list2):
#     print(item)
# print(max(list2))
# print(min(list1))

# from random import shuffle

# list = [1,2,3,4,5]
# random.shuffle(list)

# list = [num**2 for num in range(0,11)]
# print(list)
# for x in [2,3,4]:
#     for y in [4,5,6]:
#         print(x*y)

#paremeter passing in function
# def dog_check(mystring):
#     if 'dog' in mystring.lower():
#         print('ok')
#         return True
#     else:
#         print('not ok')
#         return False
# dog_check('I have pet Dog')

# def myFunc(*args):
#     for item in args:
#         print(item)
# myFunc(10,20,22,30)

# def my_func(**kwargs):
#     print(kwargs)
#     if 'fruit' in kwargs:
#         print('My favorite fruit is {}'.format(kwargs['fruit']))
#     else:
#         print('This is not my favorite fruit')
# my_func(fruit = 'apple', vegge = 'mango',food = 'biriany' )

# def my_func(*args,**kwargs):
#     print(args)
#     print(kwargs)
#     print('The key argument is {} {} '.format(args[1],kwargs['number']))
# my_func(10, 11, 33, word = 'nothing', number = 'number', class1 = 'class')

#map method
def square(num):
    return num**2
my_num = [1,2,3,4]
#show the memory location
print(map(square,my_num))
#showing the output
for item in map(square,my_num):
    print(item)
print(list(map(square,my_num)))
