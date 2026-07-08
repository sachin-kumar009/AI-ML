#1
M=int(input("Enter marks: "))
if 41<=M and M<=50:
    print("A")
elif 31<=M and M<40:
    print("B")
elif 21<=M and M<30:
    print("C")
elif 11<=M and M<20:
    print("D")
elif 10>=M:
    print("E")
else:
    print("Error")

#2

chr=input("Enter character: ")
if chr=='P'or chr=='p':
    print("PrepBytes")
elif chr=='Z'or chr=='z':
    print("Zenith")
elif chr=='E'or chr=='e':
    print("Expert Coder")
elif chr=='D'or chr=='d':
    print("Data Structures")
else:
    print("Error")

#3
a=int(input('Enter first number: '))
b=int(input('Enter second number: '))
c=int(input('Enter third number: '))
if a>b and a>c:
    print(a)
elif b>a and b>c:
    print(b)
else:
    print(c)

#4
a=int(input('Enter first number: '))
b=int(input('Enter second number: '))
c=int(input('Enter third number: '))
if a<b and a>c:
    print(a)
elif b<a and b>c:
    print(b)
else:
    print(c)

#5
a=int(input('Enter first number: '))
b=int(input('Enter second number: '))
c=int(input('Enter third number: '))
if a>90 or b>90 or c>90:
    print("obtuse")
else:
    print("acute")