# Strings: ordered, immutablem text representation

my_string = "Hello World"
print(my_string)

# for multiple line string, \ can prevent change of line
my_string = '''Hello \
world2
'''

print(my_string)

char = my_string[0]
print(char)

# we cannot change a char in the string as they are immutable

greeting = "Hello"
name = "Tom"
sentence = greeting + " " + name
print(sentence)

for i in greeting:
    print(i)

if 'ell' in greeting:
    print("Yes")
else:
    print("No")



# we can use strip to get rid of the whitespaces

string1 = '    Hello World    '
my_string_strip = string1.strip()

print(my_string_strip)

print(my_string.lower())
print(my_string.upper())

print(my_string)
print(my_string.startswith('Hello'))
print(sentence.endswith('Tom'))

#return first index of the char or a substring
print(sentence.find('lo')) 

print(sentence.count('o'))

print(sentence.replace('hello','welcome'))

# to split the sentence in the list of words
message = 'how,are,you,doing'
my_list = message.split(",")

#to join elements of the list to a string
new_message = ' '.join(my_list)
print(new_message)

my_list2 = ['a'] * 6
print(my_list2)

my_str = ''.join(my_list2)
print(my_str)


#formatting a string
#%, .format(), f-Strings

var = "Tom"
my_string = "the variable is %s" % var
print(my_string)

# %d for integer, %f for float

var = "Tom"
var2 = 6.3434
my_string = "the variable is {} and {:.2f}".format(var,var2)
print(my_string)

var = "Tom"
my_string = f"the variable is {var} and {var2}"
print(my_string)

