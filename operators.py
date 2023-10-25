# arithmetic operators

a=4
b=6
print(a+b)  #add
print(a-b)  #subtract
print(a*b)  #multiply
print(a/b)  #divide
print(a%b)  #remainder

#Comparison operators

c=56
d=21

print(f"{c} is equal to {d} {c == d}")   #equal to (==)
print(f"{c} is not equal to {d} {c!= d}")  #not equal (!=)
print(f" {c} is greater than {d} {c >d}")  #greater than (>)
print(f"{c} is greater than or equal{d} {c >= d}") #greater than/equal to (>=)
print(f"{c} is less than {d} {c <d }") #less than (<)
print(f"{c} is less than or equal to {d} {d <= c}") #less than or equal to (<=)

#logical operator - and/or
e=7

print(e>4 and e>7) #both conditions (greater/ less than need to be true)
print(e>4 or e<7)  #only one condition needs to be true (either greater or less than)