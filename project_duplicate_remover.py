def remove_duplicates(lst):
    """Removes duplicates from a list while maintaining order."""
    seen = set()
    unique_list = []

    for item in lst:
        if item not in seen:
            seen.add(item)
            unique_list.append(item)

    return unique_list

# Example usage
my_list = [1, 2, 2, 4,3, 4, 5, 6, 6, 8, 7, 9, 9]
print("Original List:", my_list)
print("List After Removing Duplicates:", remove_duplicates(my_list))



new_unique_list = list(set(my_list))
print(new_unique_list)
