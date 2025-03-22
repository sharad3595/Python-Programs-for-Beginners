a = [1,2,4,5,6,7,8,9]

#======= missing value using summation method =======
n = a[-1]
total = n* (n+1)//2

n_sum = sum(a)

missing_value = total - n_sum
print(missing_value)

#======= missing value using XOR method =======
arr_len = len(a)
xor_a = a[0]
for index in range(1,n-1):
    xor_a = xor_a^a[index]
    print(xor_a)

