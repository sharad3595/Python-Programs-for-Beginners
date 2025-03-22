
#positional argument examples
#using functions with arguments without annotations
print("-------------------------------")
print("functions with arguments but without annotation")
def find_vowels(user_input):
    vowels = set('aeiou')
    return sorted(vowels.intersection(user_input))

user_input = input("please enter a text: ")
print(find_vowels(user_input))


#using functions with arguments and annotations
print("-------------------------------")
print("functions with arguments and annotation")
def search4letters(phrase:str,letter:str) -> set:
    #remember set returns values with no duplicate
    return set(letter).intersection(set(phrase))

print(search4letters('hello dear','aeiou'))

#keyword argument examples
print("-------------------------------")
print("functions with keyword argument")
def keyword_arg_function(letters='aeiou',phrase='purple')->set:
    return set(letters).intersection(set(phrase))

print(keyword_arg_function())
