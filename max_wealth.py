

def max_wealth(ar):
    sum_array = []
    mwealth = 0
    for row in range(len(ar)):
        for ele in range(len(ar[row])):
            mwealth = mwealth + ar[row][ele]
        sum_array.append(mwealth)
        mwealth = 0    
   
    print(max(sum_array[:]))
    


A = [[1,5],[7,3],[3,7]]
max_wealth(A)


