list_with_duplicate_values = [1,2,3,1,4,7,5,6,6,3,4,5,9,10,1,2,3,8,7]
set_with_unique_values = set()
for index in range(len(list_with_duplicate_values)):
    if list_with_duplicate_values[index] not in set_with_unique_values:
        set_with_unique_values.add(list_with_duplicate_values[index])


print(set_with_unique_values)


new_set_with_unique_values = set(list_with_duplicate_values)

print(new_set_with_unique_values)
