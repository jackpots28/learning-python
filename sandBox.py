# prints on single line
for i in range(0, 10):
    print(i, end=" "),
print("\n")


# prints on sequential lines
for j in range(1, 10):
    print(j)
print()


# --tuples are like lists but are immutable--
# --playing with lists --

# makes list and appends 1-9 to list
list_List = []
for a in range(1, 10):
    list_List.append(a)
print(list_List, end="\n\n")


# appends only even number 1-30 to list using if
new_list = []
for b in range(1, 30, 1):
    if((b % 2) == 0):
        new_list.append(b)
print(new_list, end="\n\n")


# --dictionaries are like lists but more similar to c++ unordered_maps--
# --playing with dictionaries--

# declare a dictionary and initialize key value pairs
empty_Dic = {
    'key' : 'value',
    'key2' : 'value2'
}
print(empty_Dic, end="\n")

# change value of a key by referencing ['key']
empty_Dic['key'] = 'new value'
print(empty_Dic, end="\n\n")

print(list(empty_Dic.items())) # list of all key value pairs
print(list(empty_Dic.keys())) # list of all keys
print(list(empty_Dic.values())) #list of all values