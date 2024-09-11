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