#!/usr/bin/env python
# coding: utf-8

ice_cream_rating = 10
sleeping_rating = 10

print('Enter your first name')
first_name = input()

print('Enter your last name')
last_name = input()


my_name = first_name  + ' ' + last_name

print(my_name)

happiness_rating = ((ice_cream_rating + sleeping_rating) / 2)


print(type(ice_cream_rating))
print(type(first_name))
print(type(happiness_rating))

''' The happiness_rating type surprised me.  I thought it would return an integer type but instead it was converted to a float
'''


# To calculate happiness percentage as an average between ice cream rating and sleeping rating

happiness_percentage = (happiness_rating) / ((ice_cream_rating + sleeping_rating) /2)


# final statement of facts
print('My name is', first_name, 'and I give eating ice cream a score of' , ice_cream_rating , 'out of 10!')
print('I am', my_name, 'and my sleeping enjoyment rating is', sleeping_rating, '/ 10')
print('Based on the factors above, my happiness rating is', happiness_rating, 'out of 10', 'or', format(happiness_percentage,'.2%'))