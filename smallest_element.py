arr = [30,6,32,35,21,10,5,7,8,22,33,1]
small = arr[0]

for i in range(1,len(arr)):
    if arr[i] < small :
        small = arr[i]

print(small)
