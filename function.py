def maria():
    print("Helo there, welcome to function class.")

#calling a function
maria()
maria()

def add():
    num=int(input("Enter First Number:"))
    num2=int(input("Enter Second Number:"))
    print(f"sum of variable {num} and {num2} is {num + num2}")

def check_is_odd_even():
    nambari=int(input("Weka nambari:"))
    if nambari %2==0:
        print(f"The {nambari} is even")
    else:
        print(f"The {nambari} is an odd number")
add()
check_is_odd_even()





