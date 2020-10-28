from itertools import permutations
import enchant 


def word_conjugation():
    #using dictionary from enchant module, so that words makes sense
    d=enchant.Dict("en-US")
    op = set()

    print("Enter a word:")
    word = input()
    lettr = [x.lower() for x in word]

    for n in range(3,len(word)):
        for y in list(permutations(lettr,n)):
            z="".join(y)
            if d.check(z):
                op.add(z)
    return op

print(word_conjugation())