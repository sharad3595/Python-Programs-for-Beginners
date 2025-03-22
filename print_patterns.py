print("===== Half Pyramid =====")

for i in range(1,10):
    print('* '*i)

print('===== inverted half pyramid ========')
for i in range(10,1,-1):
    print('* '*i)


print('===== full pyramid =====')
for i in range(5):
    for s in range(-6, -i):
        print(" ", end="")
    for k in range(i+1):
        print("* ", end="")
    print()

print('===== full inverted pyramid =====')
for i in range(5):
    for s in range(i):
        print(" ", end="")
    for j in range(i, 5):
        print("* ", end="")
    print()
        
