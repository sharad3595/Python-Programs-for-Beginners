def swap_list(lst):
    list_len = len(lst)
    temp = lst[list_len - 1]
    lst[list_len-1] = lst[0]
    lst[0]=temp
   
    return lst

new_list = [10,9,8,7,22]
print(swap_list(new_list))

print('************ OR simply ***********')

def swap_list2(lst):
    lst[0],lst[-1]=lst[-1],lst[0]
    return lst
    

new_list = [10,9,8,7,22]
print(swap_list2(new_list))
