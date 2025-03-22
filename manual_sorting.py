lst_array = list([10,9,20,12,17,84,75,6])

for i in range(0,len(lst_array)-1):
    for j in range(0,len(lst_array)-i-1):
        if(lst_array[j] > lst_array[j+1]):
            temp = lst_array[j]
            lst_array[j] = lst_array[j+1]
            lst_array[j+1] = temp



print(lst_array)
