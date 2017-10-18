# Name: Fangzhou Yang
# hw3.py

##### Template for Homework 3, exercises 1 -  ######
import math
import random

# ********** Exercise 1 ********** 

# Define is_divisible function here
##### YOUR CODE HERE #####
def is_divisible(m,n):
    if n == 0:
        return False
    if m%n==0:
        return True
    return False
is_divisible(10,5)

# Test cases for is_divisible
## Provided for you... uncomment when you're done defining your function

#Firstly, we should defind that the n should not equal to zero, so if n equals 
#to zero, we should print False; next, we define that if m is divisible by n,
#we print True, otherwise False.
#So from the test above, we cansee that when m = 8, n =4,  m is divisible by n,
#return True; when m - 8, n = 3 ,  m is not divisible by n, return False; when
#n = 0, since we have defined that n could not equal to zero, return False.

print(is_divisible(10,5))  # This should return True
print(is_divisible(18,7))  # This should return False
print(is_divisible(42,0))  # What should this return? False

# ********** Exercise 2 ********** 

# Define not_equal function here
##### YOUR CODE HERE #####
def not_equal(x,y):
    if x==y:
        return "False, they are equal"
    else:
        return "True, they are not equal"
# Test cases for not_equal
##### YOUR CODE HERE #####
print(not_equal(5,5))
print(not_equal(5,3))


# ********** Exercise 3 ********** 

## 1 - multadd function
##### YOUR CODE HERE #####
import math

def multadd(a,b,c):
    return a*b+c


## 2 - Equations
##### YOUR CODE HERE #####
angle_test = multadd(math.cos(math.pi/4),1/2,math.sin(math.pi/4))
ceiling_test = multadd(math.log(12,7),2, math.ceil(276/19))

# Test Cases
# angle_test =
print("sin(pi/4) + cos(pi/4)/2 is:")
print(angle_test)

# ceiling_test =
print("ceiling(276/19) + 2 log_7(12) is:")
print(ceiling_test)


# ********** Exercise 4 **********

## 1 - rand_divis_3 function
##### YOUR CODE HERE #####
def rand_divis_3():
    g = random.randint(0,100)
    print(g)
    if g%3==0:
        return True
    else:
        return False

# Test Cases
##### YOUR CODE HERE #####
for i in range(3):
    print(rand_divis_3())
