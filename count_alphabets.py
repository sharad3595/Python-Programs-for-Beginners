def count_letters():
    uinput = input("enter a word: ")
    lst = list(uinput)
    dict = {}
    for i in lst:
        if i not in dict.keys():
            dict[i] = 0
        dict[i]= dict[i]+1
    print(dict)


count_letters()
