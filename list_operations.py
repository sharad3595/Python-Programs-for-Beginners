# Initialize an empty list
a = []

# Adding 10 to end of list
a.append(10)  
print("After append(10):", a)  

# Inserting 5 at index 0
a.insert(0, 5)
print("After insert(0, 5):", a) 

# Adding multiple elements  [15, 20, 25] at the end
a.extend([15, 20, 25])  
print("After extend([15, 20, 25]):", a) 


# updating list elements
a = [10, 20, 30, 40, 50]
print('original List: ', a)

# Change the second element
a[1] = 25 

print("after update:",a)


# Removes the first occurrence of 30
a.remove(30)  
print("After remove(30):", a)

# Removes the element at index 1 (20)
popped_val = a.pop(1)  
print("Popped element:", popped_val)
print("After pop(1):", a) 

# Removes last index
popped_last = a.pop()  
print("Popped kast element:", popped_last)
print("After last pop():", a) 

# Deletes the first element (10)
del a[0]  
print("After del a[0]:", a)  
