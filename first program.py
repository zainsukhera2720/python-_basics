print(23)
print(35+23)
a=50
b=23
print(a!=b)
print('My name is zain', 'My age is 19')
print("Python",'Language')
print("Hello World",'The Language first program') 
print("Computerlanguage:,Python")
name='zain'
age='18'
price='12.99'
print(name)
print(age) 
print(price)
print('my name:',name)
print('age:',age)
print('price:',price)
age2=age
print("age:",age2)
print(type(name)) 
print(type(age))
print(type(price))
age=23
old=False
a=None
print(type(old))
print(type(a))
a=5
b=2
sum=a+b
print(sum)
# print('Hello world')
# arthimetic operator

a=5
b=2
print(a%b) 
print(a**b)

# realtional operator
a=50
b=20
print(a==b)
print(a>=b) #YA
print(a<=b)

# assigment operator

num=60
num+=20
print("num:",num)
num=50
num**=25
print("num:",num)

# logical operator 

a=25
b=5
print(not False)
print(not True)

print(not(a>b))
#  And operator
val1=50
val2=5
print("and operator:",val1 and val2)
# example of and operator
print(5 and 10)
print(0 and 10)

# or operator
print("or operator:",val1 or val2)

print("or operator:",(a==b)or(a>b))
print("and operator:",(a==b)and(a>b))
print("or operator:",(a==b)or(a>b))
print("or operator:",(a==b)or(a>b))
print("or operator:",(a==b)or(a>b))
print("or operator:",(a==b)or (a>b))

# type conversion
a=int('2')
b=4.20
print(a+b)
a=3.14
a=str(a)
print(type(a))
name=input("enter your age")
print("you entered:",name)
val=(input("enter some value")) 
print(type(val),val)  
val=float(val)
print(type(val))
# string and conditional statments
str8="This is a string.\n we are creating in python"
print(str8)
str9="this is a string.\twe are creating in python"
print(str9)
str3="Uol"
str4="AI"
final_str=(str3+str4)
print(final_str)
# len(str)
str5="husnain"
print(len(str5))
# second method
str6="husnain"
len6=len(str6)
print(len6)
str7="haider"
len7=len(str7)
print(len7)
final_str=(str6 +" "+ str7)
print(len(final_str))
str9="this is string\nwe are creating in vs code"
str12="apna"
len12=len(str12)
print(len12)
str13="college"
len13=len(str13)
print(len13)
final_str=(str12+str13)
print(len(final_str))
# indexing
str="zain haider"
ch=str[3]
print(ch)
str="australia city"
print(str[0:9])
print(str[10:14])
print(str[5:12])
print(str[:9])
print(str[0:14:2])
print(str[3:3])

# slicing question
my_list=[5,10,15,20,25]
print(my_list[-4:-1])
# question
nums=[0,1,2,3,4,5,6,7,8,9]
print(nums[5:])
str="apna college"
print(str.endswith("ge"))
str="ali is Bad boy"
str=(str.capitalize())
print(str)
age=94

if age>=18:
    if age>=80:
        print("cannot drive")
    else:
        print("can drive")
else:
    print("cannot drive")
num=int(input("enter a number"))
if num%2==0:
    print('E')
else:
    print("O")    


