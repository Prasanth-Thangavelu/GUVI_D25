#!/usr/bin/env python
# coding: utf-8

# # 1. Python program to check whether the given number is even or not.

# In[ ]:


userinput = int(input("Enter the Value"))
print("Given Number : "+userinput)
if(userinput %2 == 0):
  print("Give number is Even")
else:
  print("Given number is NOT Even")


# # 2. Python program to convert the temperature in degree centigrade to Fahrenheit.

# In[ ]:


Fahrenheit = float(input("Enter the temperature in Fahrenheit "))
Celsius =((Fahrenheit-32)*5)/9
print("Temperature in Celsius : " , Celsius)


# # 3. Python program to find the product of a set of real numbers.

# In[ ]:


productset = 1
NumberCount = int(input("Enter the number of real numbers: "))
for i in range(NumberCount):
    ProductValue = float(input("Enter a real number: "))
    productset = productset * ProductValue
print("The product of real number is: ", productset)


# # 4. Python program to find the factorial of a number using recursion.
# 

# In[ ]:


def factorial(n):
    return 1 if (n==1 or n==0) else n * factorial(n - 1);

userinput = int(input("Enter the Value"))

print("Factorial of",userinput,"is",
factorial(userinput))


# # 5. Python program to implement linear search.
# 

# In[ ]:


Numberset=[2,3,5,6,7,8,9,0,1,4]
userinput = int(input("Enter the Value : "))
for i in range(len(Numberset)):
  if (userinput == Numberset[i]):
    print("Given number found in location : ", i)
    NumberLoc=Numberset[i]
    break
  else:
    NumberLoc=0

if(NumberLoc==0):
  print("Number Not found in the Set")


# # 6. Python program to implement binary search.
# 
# 

# In[ ]:


def binarySearch(numbers, lowvalue, highvalue, Userinput):
    if (highvalue >= lowvalue):
        mid = lowvalue + (highvalue - lowvalue)//2
        if (numbers[mid] == Userinput):
            return mid
        elif (numbers[mid] > Userinput):
            return binarySearch(numbers, lowvalue, mid-1, Userinput)
        else:
            return binarySearch(numbers, mid+1, highvalue, Userinput)
    else:
        return -1
numbers = [2,3,5,1,7,8,9,10,16,44]
Userinput = int(input("Enter the Value : "))
result = binarySearch(numbers, 0, len(numbers)-1, Userinput)
if (result != -1):
    print("Search successful, element found at position ", result)
else:
    print("The given element is not present in the array")


# # 7. Python program to find the largest number in a list without using built-in functions.
# 

# In[ ]:


Input = [2,21,5,11,7,18,9,10,16,4]
BigNum = 0 
for i in Input:
  if(i>BigNum):
    BigNum = i
print("Biggest Number is : ",BigNum)


# # 8. Python program to delete an element from a list by index.
# 

# In[ ]:


numbers = [3,4,1,9,6,2,8]
print(numbers)
x = int(input("Enter the position of the element to be deleted: "))
numbers.pop(x)
print(numbers)


# # 9. Python program to print all the items in a dictionary.
# 

# In[15]:


Dic1 = {'TATA':'Altroz', 'Honda' :'Jazz', 'Hyundai': 'i10', 'Audi': 'A6'}
for key, value in Dic1.items():
    print(key + " : " + value)


# # 10. Python program to find the average of 10 numbers using while loop.
# 

# In[19]:


count,Total = 0,0 
while count<10:
    userinput = int(input("Enter the number to sum : "))
    count = count+1
    Total = Total+userinput
    
avg=Total/10

print("Average of 10 numbers : ",avg)
    


# In[ ]:




