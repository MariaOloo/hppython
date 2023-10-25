num= int(input("Enter Number"))
num2= int(input("Enter to check whether number is odd or even"))

if num>0:
    print(f"The {num} is positive")
else:
    print(f"The {num} is negative")

if num2 %2==0:
    print(f"The {num2} is even")
else:
    print(f"The {num2} is odd")