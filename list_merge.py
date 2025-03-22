# straight forward way
a = [1, 2, 3]
b = [4, 5, 6]

# Merge the two lists and assign
# the result to a new list
c = a + b
print(c)


#using extend()
a = [1, 2, 3]
b = [4, 5, 6]

# Add all elements from list 'b' to the end of list 'a'
a.extend(b)

print(a)
