
#========= find duplicate alphabets ===============
user_input = input(f"Enter a sentence: ")
lst_user_input = list(user_input)
new_list = []
dup_list = []


for i in lst_user_input:
    if i not in new_list:
        new_list.append(i)
    else:
        dup_list.append(i)

print(dup_list)
