# sets hold unique sets of values, like dictionary and list, sets can grow and shrink
vowels = {'a','u','e','i','o'}
word = 'hello'
u = vowels.union(set(word))#combine with vowel set
print(u)

#get sorted list of unique letters
sorted_new_list = sorted(list(u))
print(sorted_new_list)

#get difference between two sets
#returns a new set of objects (called d here) 
#which are in the vowels set but not in set(word). 
diff = vowels.difference(set(word))
print(diff)

#get intersetion values between two sets
common = vowels.intersection(set(word))
print(common)


#set based vowels search program
print('search vowels using sets')
vowels = set('aeiou')
search_word = input("input a text to search for vowels")
found = vowels.intersection(set(search_word))
print(found)
