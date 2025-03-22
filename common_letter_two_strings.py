input1 = input("enter a word: ")
input2 = input("enter second word: ")
input1_set = set(input1)
input2_set = set(input2)
print(input1_set.intersection(input2_set))


#============= OR =============

#defining function is not necessary but for variation i am using
def common_letter():
    w1 = input("Enter first word: ")
    w2 = input("Enter second word: ")

    s1 = set(w1)
    s2 = set(w2)

    cmn_letters = s1 & s2
    print(cmn_letters)


common_letter()
