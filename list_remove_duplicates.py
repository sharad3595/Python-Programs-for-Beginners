a = [10,20,30,10,10,30,40,50,60,70,50]
new_a = []

for i in range(len(a)-1):
    for j in range(len(a)-1):
        if( a[i] not in new_a):
            new_a.append(a[i])



print(a)
print(new_a)
