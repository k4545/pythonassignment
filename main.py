x=int(input("enter first number:"))
y=int(input("enter second number:"))
z=int(input("enter third number:"))
if(x>y)and(x>z):
    print("large number",x)
elif(y>x)and(y>z):
    print("large number",y)
else:
    print("large number",z)
