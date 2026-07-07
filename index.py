print("Hello")
a=23
print(a)
print(type(a))
list1=[1,2,3,4,5]
print(list1)
list1.append(6)
print(list1)

list1.remove(6)
print(list1)

tup=(2,3,4,5)
print(tup)

set1={2,3,4,5}
print(set1)

dic={"name": "Sachin","age":21}
print(dic)

a=100
b=23
res=a+b
print(res)

res=a%b
print(res)

res=a**b
print(res)

res=a//b
print(res)

a=20
b=4
res= a<=b
print(res)

res=a<b
print(res)

print(not True)

print(a>2 and b<=4)
print(a>2 or b>4)
print(a>2 or b<4)
print(a<2 or b>=4)
print(a<=2 or b==5)

num=23
num1=+4
num+=4
print(num,num1,sep='\n')

print(a!=b)
print(a is b)
print( a is not b)

list1=[2,3,4,5,6,7,8]
res=5 in list1
print(res)
res1=5 not in list1
print(res1)

x=10
y=12
if x>y:
    print("more")
elif x!=y:
    print("not equal")
elif x==y:
    print("Equal")
else:
    print("less")


for i in range(5,10,2):
    print(i)