my_string = 'Київ Одеса Львів'.endswith('Львів')
my_string2 = 'Київ Одеса Львів'.startswith('Київ')

list_of_cities = 'Київ Одеса   \n Львів'.split()
print(list_of_cities)
print(my_string)
print(my_string2)


empty_list1 = []
emtpy_list2 = list()


list_of_products = [
    'chesse',
    'broccoli',
    'bread',
]

print(list_of_products)

first_product = list_of_products[0]
print(first_product)

for product in list_of_products:
    print(product)
    print(1111111)

last_product = list_of_products[-1]
two_product = list_of_products[1:]

sister_list = [
    'lipstick',
    '',
    '',
]

# delete element
list_of_products.remove('bread')
data = list_of_products.pop(0)
data1 = list_of_products.pop() 

# add elements
list_of_products.append('milk')
list_of_products.append('milk2')
list_of_products.insert(0, 'beer')

# for product_from_sister in sister_list:
#     list_of_products.append(product_from_sister)

list_of_products.extend(sister_list)
list_of_products.extend('fffff749124')

my_sentence = 'I Love python'
last_letter = my_sentence[-1]

for letter in my_sentence:
    if letter.islower():    
        print(letter.upper())

