def swap_func(p1,p2,lst):
    lst[p1],lst[p2]=lst[p2],lst[p1]
    return lst


swap_list = [10,20,30,40,50,60]
pos1, pos2 = 2,5
print(swap_func(pos1,pos2,swap_list))
