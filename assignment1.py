#question 1

num1=2
num2=2
num3=3

avg=(num1+num2+num3)/3

print("the average of three numbers is",avg)


#question 2
a=int(input("enter gross income- $"))
b=int(input("enter the number of dependents-"))
c=a-10000-(b*3000)
t=c*0.2
print("your tax is $",t)


#question 3
a=int(input("enter number of seconds="))
b=a//60
c=a%60
print(a,"seconds is", b,"minutes and",c, "seconds")
        

#question 4
a=int(25)
b=float(25.0)
c=float(str("25"))
d=str(a+b+c)
print(d)
print(type(d))

#question5
from math import*
for i in range(0,360,15):
        print(i,round(sin(i),4),round(cos(i),4))
