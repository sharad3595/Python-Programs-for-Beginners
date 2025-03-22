def get_anagrams(A):
    new_list = {}
    for i in range(len(A)):
        '''join is used here because sorted() returns a list,
        here we are converting list ofevery single word alphabet
        to string again'''
        word = ''.join(sorted(A[i]))
        if (word not in new_list):
            new_list[word] = [i +1]
        else:
            new_list[word].append(i+1)
    print(new_list)
        
    
anagrams = ['cat','dog','tca','act','god']
get_anagrams(anagrams)
