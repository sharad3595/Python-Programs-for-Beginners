sentence = "nancy is 90 years old. she wants 120 toffees"
num = []

for word in sentence.split():
    if word.isdigit():
        num.append(word)

print(num)

#========= is digit don't get float values so we will use isalpha() =====


sentence2 = "nancy is 90 years old she wants 12.5 toffees"
num2 = []
for word in sentence2.split():
    if not word.isalpha():
        num2.append(word)

print( num2)

#======= isalpha() also catches .,;,and comma etc =========
# use regex
