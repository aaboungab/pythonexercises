a=str(input("Input first word: "))
b=str(input("Input second word: "))

def near(word1, word2):
    try:
        if len(word1) - 1 > len(word2):
            return False
        for i in range(0, len(word1)):
            matching = word1[0:i:] + word1[i + 1::]
            if matching == word2:
                return(True)
        else:
            return False
    except:
        print("somthing went wrong")

print(str(near(a,b)))