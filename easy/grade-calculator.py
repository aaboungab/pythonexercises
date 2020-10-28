print('Hi, what is your name?')
name = str(input())
print("Hello there", name, '!')

#get marks for modules 
print('What is your maths mark? /100')
mathsmark = int(input())
print('What is your chemistry mark? /100')
chemistrymark = int(input())
print('What is your physics mark? /100')
physicsmark = int(input())

#total mark calculator 
totalmark = ((mathsmark+chemistrymark+physicsmark)/300)*100

#depending on totalmark output is specific grade
if totalmark >= 70:
    print("Your final grade is A")
elif totalmark >= 60:
    print("Your final grade is B")
elif totalmark >= 50:
    print("Your final grade is C")
elif totalmark >= 40:
    print("Your final grade is D")
else:
    print("You have failed!")

#format output to user
print(f"{name} your final mark is {totalmark:.2f}%")
