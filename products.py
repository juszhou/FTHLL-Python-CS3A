"""
Program #: Progamming Project 6A
Programmer: Justin Zhou
Due: 08/02/2021
CS 3A, Summer 2021
Description: (Create a Products python file demonstrating your knowledge of loops)
"""

#number function
def get_number():
    while True:
        num_of_prod = int(input(
            'Enter the number of products you would like to add.\nEnter 0 (zero) if you do not wish to add products:'))
        if num_of_prod == 0:
            break
        elif num_of_prod < 0:
            print('Incorrect data type entered!')
            num_of_prod = int(input(
                'Enter the number of products you would like to add.\nEnter 0 (zero) if you do not wish to add products:'))
        else:
            break
    return num_of_prod

#string intializer and more
max_size = get_number()

if max_size == 0:
    print('No products required!')
else:
    products = []
    for i in range(max_size):
        products.append(i)

for i in range(len(products)):
    products[i] = input('Please enter the product name:')

#displayer prints list
def display_products(list):
    for i in range(len(list)):
        print(list[i])

#sorts list using selection sort by finding smallest value and move it to the front of the list
def sort_products(list_to_be_sorted):
    for n in range(len(list_to_be_sorted)):
        min_index = n
        min_str = list_to_be_sorted[n]
        for j in range(n + 1, len(list_to_be_sorted)):
            if min_str > list_to_be_sorted[j]:
                min_str = list_to_be_sorted[j]
                min_index = j
        if not min_index == n:
            temp = list_to_be_sorted[n]
            list_to_be_sorted[n] = list_to_be_sorted[min_index]
            list_to_be_sorted[min_index] = temp
    return list_to_be_sorted
print('Unordered list')
print('--------------------')
display_products(products)
print('Ordered list')
print('--------------------')
ordered_products = sort_products(products)
display_products(products)

#searches
def search_products(searchlist, keyword):
    for i in range(len(searchlist)):
        if searchlist[i].lower() == keyword.lower():
            return i
        else:
            return -1

keyword = input(
    "Enter a product's name, or N if you do not wish to enter a product's name:")

if keyword != 'N':
    key_pos = search_products(products, keyword)
if key_pos == -1:
    print(keyword, " is not one of the product's name")
else:
    print(keyword, "is one of the product's.\nthe position is ", key_pos+1)



""" ------------------- Sample Run --------------------
Enter the number of products you would like to add.
Enter 0 (zero) if you do not wish to add products:6
Please enter the product name:Folders
Please enter the product name:calculator
Please enter the product name:binder
Please enter the product name:backpack
Please enter the product name:erasers
Please enter the product name:calender
Unordered list
--------------------
Folders
calculator
binder
backpack
erasers
calender
Ordered list
--------------------
Folders
backpack
binder
calculator
calender
erasers
Enter a product's name, or N if you do not wish to enter a product's name:Folders
Folders is one of the product's.
the position is  1

Process finished with exit code 0
---------------------- End Sample Run ----------------"""