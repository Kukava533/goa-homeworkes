
from urllib import response


while True:
    print("continue? Y/N")
    response = input()
    if response.lower()== 'y':
        continue
    break
string = "port of georgia "
new_string = string.capitalize()
print(new_string)
print(string)

str_1 = "never test bath water whith both feet"
index_positions = str_1.find("whith")
print(index_positions)

list =['m','c','o']
a = 'MCO'
a.join('m', 'c','o')
a = "-"
a.join("mco")
'M-C-O'


# the split() method splits a string into a list of substrings called tokens.
# 1. all the tokens combined from the larger string if put together
# 2. a separator character indicated where to split up the string, to create the tokens.

# the join() method glues together a bunch of substrings into one big string
# the split() and join() methods are somethimes used together


