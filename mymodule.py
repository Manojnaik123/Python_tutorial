# '''
# #
# ##
# ###
# ####
# #####
# '''
# from functools import reduce
#
# rows= 5
# for x in range(1, rows+1):
#     for y in range(x):
#         print('#', end='')
#     print()
#
# for x in range(1, rows+1):
#     print('#'*x)
#
#
# # reverse pattern
# '''
# #####
# ####
# ###
# ##
# #
# #####
# ####
# ###
# ##
# #
# '''
# rows = 5
# for x in range(rows):
#     print('#'*(rows - x))
#
# for x in range(rows):
#     for y in range(rows - x):
#         print('#', end='')
#     print()
#
# # Pyramid pattern
# '''
#                    *
#                   ***
#                  *****
#                 *******
# '''
# rows = 5
# for x in range(rows):
#     for y in range(rows - (x+1)):
#         print(' ', end='')
#     for z in range(2*(x+1) - 1):
#         print('*', end='')
#     print()
#
# '''
# *********
#  *******
#   *****
#    ***
#     *
# '''
# rows = 5
# for x in range(rows):
#     for y in range(x):
#         print(' ', end='')
#     for z in range(2*rows - (2*(x+1) - 1)):
#         print('*', end='')
#     print()
#
# # prime umber finding
# #Prime number- number greater than 1 and is divisible by itself and 1
#
# num = 5
#
# if num > 1:
#     for x in range(2, num):
#         if num % x == 0:
#             print('not a prime')
#             break
#     else:
#         print('Prime number')
# else:
#     print('Not a prime')
#
# # Filter reduce and map in python
# '''
# map() → Transform each element (e.g., square numbers).
#
# filter() → Select elements based on condition (e.g., only evens).
#
# reduce() → Aggregate results into a single value (e.g., sum/product).
# '''
#
# a = [1,2,3,4,5]
# # the map function retuns object so conver it into list
# b = list(map(lambda x : x*2, a))
# print(b)
#
# # Convert the result object into list
# c = list(filter(lambda x : x >=3, a))
# print(c)
#
# # Reduce will club the entire list value into one
# d = reduce(lambda x,y: x+y, a)
# print(d)
#
# x = [1,2,3,4,5]
# y = (7,8,9)
#
# # Zip function
# # this function will combines multiple sequences element by element
# z= list(zip(x,y))
# print(z) # prints - [(1, 7), (2, 8), (3, 9)]
#
# # Unzipping
# zipped = [(1, 7), (2, 8), (3, 9)]
# first, last = zip(*zipped)
# print(first) #(1, 2, 3)
# print(last) #(7, 8, 9)

s = '{1} + {0} = {2}'

print(s.format(2,1,3))

