'''
GOOGLING CHALLENGE! 

Today, we'll ask you to write a bunch of small pieces of code.

Unlike previous ones, we have NOT showed you the exact code you'll need to answer the questions.

So, you'll want to search out answers on the web, make sure you understand them, then try them out until they work!

For each question, you should also COPY THE LINK TO THE RESOURCE WHERE YOU FOUND THE SOLUTION in so that you can use it in the future too
'''


# 1A. Sort the below list in alphabetical order
print('QUESTION 1\n')
my_friends = ['Yusuf', 'Aedan', 'Mia', 'Ash', 'Paul', 'Aeshna', 'Aryn', 'Rob']
# Used sorted() for alphabetical sorting from https://realpython.com/python-sort/
print(sorted(my_friends))



# 1B. Comment your code in 1A to convince yourself you understand how it works
# sorted(), without any other arguments but a list will perform a recursive sort on the list until it's in ascending order.

# 2A. Get all the keys from the below dictionary, then print them out:
# Hint: there is a single command that can do this
print('QUESTION 2\n')

my_account = {'username': 'pbloom',
			'password': 'python3.7',
			'balance': 101.8,
			'transaction_dates': ['9/18/2020', '9/20/2020', '10/5/2020'],
			'verified': True}

print(my_account.keys())

# 2B. Comment your code in 2A to convince yourself you understand how it works
# used keys() method from https://stackoverflow.com/questions/5904969/how-to-print-a-dictionarys-key


# 3A Count how many times the word 'wood' appears in the following string:
# Hint: there is a single command that can do this
print('QUESTION 3\n')
my_string = 'how much wood could a woodchuck chuck if a woodchuck could chuck wood?'
print(my_string.count('wood'))

# 3B. Comment your code in 3A to convince yourself you understand how it works
# used the string.count() method from https://www.geeksforgeeks.org/find-frequency-of-each-word-in-a-string-in-python/


# 4A Count how many times the string 'banana' appears in the following list:
# Hint: there is a way to do this with one line of code
print('QUESTION 4\n')
my_list = ['apple', 'banana', 'banana', 'cherry', 'mango', 'banana', 'banana', 'banana']
print(my_list.count("banana"))

# 4B. Comment your code in 4A to convince yourself you understand how it works
# used list.count() method from https://www.geeksforgeeks.org/python-count-occurrences-element-list/


# 5A Print out all of the unique strings in my_list
# Hint: there is a way to do this with one line of code
print('QUESTION 5\n')
print(set(my_list))

# 5B. Comment your code in 5A to convince yourself you understand how it works
# used set() function from https://www.geeksforgeeks.org/python-get-unique-values-list/

# 6A. Import numpy, then use it to generate a random number between 0-1
print('QUESTION 6\n')
from numpy.random import default_rng
print(default_rng(1).random())

# 6B. Comment your code in 6A to convince yourself you understand how it works
# numpy.random's default_rng acts as a seed for the random() method, from https://numpy.org/doc/stable/reference/random/index.html
# Like the rest of the challenge, wanted to do it in one line of code

'''
Nice job! Hopefully after doing this challenge you feel a bit more ready to be able to search out new code solutions.
We'll be doing more challenges like this coming up in the future. 

Remember to comment all your code and push your work to your Github repo when you're done!
'''
