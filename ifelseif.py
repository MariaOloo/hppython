marks=int(input("Enter Marks:"))

if marks>80 and marks<= 100:
    print("Congratulations!You got an A")
elif marks>60 and  marks<=80:
    print("Good Job!You got a B")
elif marks>40 and marks<=60:
    print("You got a C")
else:
    print("Sorry, You failed")