search_val = int(input("Please Enter search value:"))
lst = [19,10,7,20,30,15,100]
search_val_found = False
value_position = 0

for index in range(0,len(lst)):
    if(search_val == lst[index]):
       search_val_found = True
       value_position = index



if(search_val_found):
    print("Value found at position: ", value_position)
    
else:
    print("Value Not Found")
