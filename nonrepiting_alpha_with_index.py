
def repeating_alpha_with_index(str):
    dict ={}
    #new_dict will hold values with frequency 1 only
    new_dict = {}
    str_len = len(str)

    #create dictionary with the alphabet frequency from the input string
    for i in range(str_len):
        key = str[i];
        if key not in dict:
            dict[key] = 1
        else:
            dict[key] = dict[key]+1
    print(dict)

    for key,value in dict.items():
        if value == 1:
            new_dict[key] = 1
       
    print(new_dict)

repeating_alpha_with_index('The crazy brown fox jumped over the fence.')
