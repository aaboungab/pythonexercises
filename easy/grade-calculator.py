print('Hi, what is your name?')
name = str(input())
print("Hello there", name, '!')
print('What is your maths mark?')
mathsmark = int(input())
print('What is your chemistry mark?')
chemistrymark = int(input())
print('What is your physics mark?')
physicsmark = int(input())
totalmark = ((mathsmark+chemistrymark+physicsmark)/300)*100
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
print(totalmark)