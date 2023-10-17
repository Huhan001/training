# print("hello there {} talk to me now {}".format(34, 45))
# print("hello there {1} talk to me now {0}".format(34, 45))
# print("talk to me hoessee %s and let me know %d" % ("james", 34))
#
# jim = {1, 2, 3, 4, 5, 6, 7, 7}
#
# print(jim)
# tim = list(range(1, 15))
# susan = set(tim)
# print(susan)
#
# print(jim.difference(susan))
#
# # tenarry operator
# friend = True
# print("this is how it works" if friend else "this looks neat")
#
# # short circuiting
# is_magician = False
# print("you need magic" if is_magician and True else "do some magic tricks")
#
# counter = 0
# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for item in my_list:
#     counter += item
# print(counter)
#
# # enumerate a dictionary
# my_dict = {"name": "james", "age": 34, "height": 6.2}
# for key, _ in enumerate(my_dict):
#     print(key)
#
# alphabets = ["a", "b", "c", "d", "e", "f", "g", "a", "b", "c", "d", "e", "f", "g", "k", "l", "m"]
# new_alphabet = []
# for item in alphabets:
#     if item not in new_alphabet:
#         new_alphabet.append(item)
# print(new_alphabet)
#
#
# # class
# class PlayerCharacter:
#     # class object attribute
#     membership = True
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def run(self):
#         print("run")
#
#
# player2 = PlayerCharacter("sam", 45)
# print(player2.name)
#
# class Tomhardy:
#     def __init__(self, name, age):
#         if age > 18:
#             self.name = name
#             self.age = age
#         else:
#             self.age = age + 10
#             self.name = name
#
#     def shoutout(self):
#         print("{0} is older than {1}".format(self.name, self.age))
#
#     @classmethod
#     # this is a decorator
#     def adding_things(cls, num1, num2):
#         return cls("james", num1 + num2)
#
#     @staticmethod
#     def adding_things2(num1, num2):
#         return num1 + num2
#
# # introduce = Tomhardy("james", 2)
# # introduce.shoutout()
#
# introduce2 = Tomhardy.adding_things2(2, 3)
# print(introduce2)
#
# # include underscore in variable name to indicate private variable
# # inheritance
# class User():
#     def sign_in(self):
#         print("logged in")
#
#
# class toms:
#     def sayhello(self):
#         print("hello there")
#
# class wizzard(User, toms):
#     def __init__(self, name, power):
#         self.name = name
#         self.power = power
#
#     def attack(self):
#         print("attacking with power of {}".format(self.power))
#
#
# class archer(wizzard):
#     def __init__(self, simp, User, toms):
#         super().__init__(User, toms)
#     def timmy(self):
#         print("timmy is done")
#
#
# wizard1 = wizzard("james", 50)
# archer1 = archer("timmy", 30)
# print(wizard1.sayhello())
# print(archer1.sign_in())

# # map, filter, zip, reduce
# my_list = [1, 2, 3, 4, 5, 6, 7, 8]
# wtherelist = [2,3,5,6,2]
#
# def multiply_by2(thing):
#     newlist = []
#     for item in thing:
#         newlist.append(item * 2)
#     return newlist
#
# # with map you need only define the function
# def mapfuntion(item):
#     return item * 5
# print(list(map(mapfuntion, my_list)))
#
# # filter funciton. it needs to return a true value.
# def only_odd(item):
#    return  item % 2 == 0
#
# print(list(filter(only_odd, my_list)))
#
#
# # zip
# print(list(zip(my_list, wtherelist)))

# decorator


# def my_decorator(func):
#     def wrap_func(x):
#         print("++++++++++++++++++")
#         func(x)
#         print("++++++++++++++++++")
#     return wrap_func
# # a decorator supper boost a function it recieves a function an passes a function out.
#
# @my_decorator
# def hello(hello):
#     print(hello)
#
# hello("sean")
# # i do not need to pass in the decorator since im just using the function

from time import time
def perfomance(fn):
    def wrapper(*args, **kargs):
        t1 = time()
        result = fn(*args, **kargs)
        t2 = time()
        print("it took {} s long".format(t2- t1))
        return result
    return wrapper

@perfomance
def long_time():
    for i in range(10000000):
        i * 5

long_time()

