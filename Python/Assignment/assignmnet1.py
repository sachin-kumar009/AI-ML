# Assignment solution

# Question 1
a = 2
b = 5

def addTwoNumbers(a,b):
  return a+b
sum = addTwoNumbers(a,b)
print(sum)

# Question 2

def is_Valid(a,b):
  return (a<10) and (a>b)

result = is_Valid(5,3)
print(result)

# Question 3

def check(a,b):
  return (a % 10 == 0 ) or (b%10 == 0)

result3 = check(12,20)
print(result3)


# Question 4

def first_digit(n):
  return n // 1000

result4 = first_digit(4567)
print(result4)

# Question 5

def last_digit(n):
  return n%10

result5 = last_digit(4567)
print(result5)

# Question 6

def find_the_remainder(a,b):
  return b%a

result6 = find_the_remainder(2,9)
print(result6)


# Question 7

def multiply_two_number(a,b):
  return a*b

result7 = multiply_two_number(2,5)
print(result7)

# Question 8


def Sum(a,b,c):
  return a+b+c

def Average(a,b,c):
  return round((a+b+c)/3, 2)

marks_sum = Sum(50,20,100)
marks_average = Average(50,20,100)

print(marks_sum)
print(marks_average)
