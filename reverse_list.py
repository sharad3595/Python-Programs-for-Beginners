
#using slicing method
def reverse_lst(lst):
    slice_lst = lst[::-1]
    return slice_lst
    

lst = [10,20,30,40,50]
print(reverse_lst(lst))


#using reverse function

lst = [10,20,30,40,50]
lst.reverse()
print("Using reverse() ", lst)
 
print("Using reversed() ", list(reversed(lst)))
