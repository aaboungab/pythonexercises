#function to find subword within a word where a letter has been removed
def near(string_1,string_2):
    #Convert list_1 & list_2 into lists
    list_1 = list(string_1) 
    list_2 = list(string_2) 
    for index in range(len(list_1)):     
        element_to_remove = list_1[index] 
        del list_1[index] 
        if list_1 == list_2: 
            return True 
        list_1.insert(index, element_to_remove) 
    return False

word1 = input("enter first word: ") 
word2 = input("enter second word: ")
print(near(word1,word2)) 

