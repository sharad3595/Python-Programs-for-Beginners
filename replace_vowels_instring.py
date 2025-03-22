vowels = ['a','e','i','o','u','y']
input_string = input("Enter a string: ")
input_lst = list(input_string)

for i,k in enumerate(input_lst):
    for v in vowels:
        if v == k:
          indx = input_lst.index(k)
          input_lst[indx] = '$'

print(input_lst)
    
