
def ransom_note(magazine,ransomNote):
    counter = 1
    for i, v in enumerate(magazine):
        if v not in dict.keys():
            dict[v] = counter
        else:
            dict[v] = dict[v] + 1
    
    for i, v in enumerate(ransomNote):
        if v not in dict.keys():
            return False;

        if len(ransomNote) > len(magazine):
            return False
        if dict[v] >= 1:
            dict[v] -= 1
        else:
            return False
    return True
        


magazine = "effjfggbffjdgbjjhhdegh"
ransomNote = "fffbfg"

dict = {}

print(ransom_note(magazine,ransomNote))
