##List Comprehensions - Certain lists are very straightforward to create- some are even passed into your
#code as parameters and don't require any work at all. Others take a bit more effort:

#squared minus one without list comprehension
squared_minus_one = list()

for n in range(1, 11): #range(1, 11) will give me 1,2,3,4,5,6,7,8,9,10 - my for in will loop 10 timea
    squared_minus_one.append((n ** 2) - 1)
print(squared_minus_one)

#squared_minus_1 with list comprehension
squared_minus_1 = [(n ** 2) - 1 for n in range(1, 11)]
print(squared_minus_1)


#find all even numbers in list with list comprehension
def even_nums(num_list):
    num_list = [n for n in num_list if n % 2 == 0]
    print(num_list)

even_nums([1,2,3,4,5,6])

#add explaintion to each string element in list with a list comprehension
def explanation(str_list):
    str_list = [s + '!' for s in str_list]
    print(str_list)
explanation(['Hello', 'World'])

#############################################################
##Generator Expressions - are very similar to list comprehensions. They use almost identical
##syntax to produce iterable objects in a single line:

one_to_three = range(1, 4) #this will produce a range of 1,2,3

#A list comprehension uses square brackets
squared_lc = [n ** 2 for n in one_to_three]

#A generator uses parenthesis
squared_ge = (n ** 2 for n in one_to_three)

#Looping through each shows identical values
for n in squared_lc:
    print(n)

for n in squared_ge:
    print(n)

#But the objects are noi identical
print(squared_lc)
print(squared_ge)