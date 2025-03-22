person3 = {'Home Planet': 'Betelgeuse Seven',
'Occupation': 'Researcher'}
person3['age'] = 34

print(person3)


#*********** find frequency of vowels in string **********

print('############################################')
print("program with dictionary key initilization")
vowels= ['a','e','i','o','u']
ipt_string = input("Please enter a text:")
found = {} # declaring a dictionary

#dictionary key value initialization
found['a'] = 0
found['e'] = 0
found['i'] = 0
found['o'] = 0
found['u'] = 0

for letter in ipt_string:
    if letter in vowels:
        found[letter] +=1

for k,v in found.items():#iterating through the dictionary using items() function
    print (k,'is found:',v, 'times');

print('############################################')
print("program without dictionary key initilization")
#***** what if there are thousands of values to be initialized?******
#********* Hence, same algorithm without initializating the key of a dictionary
vowels= ['a','e','i','o','u']
ipt_string = input("Please enter a text:")
found = {} # declaring a dictionary

for letter in ipt_string:
    if letter in vowels:
        # directly doing this -> [found[letter] +=1] will raise a key error
        # because we are setting values for non existent key in a dictionary!!
        # thus a new approach is required
        if letter not in found:
            found[letter] = 1
        else:
            found[letter] +=1
#iterating through the dictionary using items() function
#using sorted function to sort the dictionary items
for k,v in sorted(found.items()):
    print (k,'is found:',v, 'times');
    
print('############################################')
print("program without dictionary key initilization but using setdefaults() method")

vowels= ['a','e','i','o','u']
ipt_string = input("Please enter a text:")
found = {} # declaring a dictionary

for letter in ipt_string:
    if letter in vowels:
        if letter not in found:
            found.setdefault(letter,1)
        else:
            found[letter] +=1
#iterating through the dictionary using items() function
#using sorted function to sort the dictionary items
for k,v in sorted(found.items()):
    print (k,'is found:',v, 'times');
    



        
