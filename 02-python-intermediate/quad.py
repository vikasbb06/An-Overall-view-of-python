from math import sqrt
a=int(input("The co-efficient of x^2 is :"))
b=int(input("The co-efficient of x is:"))
c=int(input("The constant is :"))
if(a!=0):
    print("The Quadratic Equation you entered is {}x^2+{}x+{}".format(a,b,c))
else:
    print("The Quadratic Equation you entered is {}x+{}".format(b,c))
d=b*b-4*a*c
if(a!=0 and b!=0) :
        if(d>0):
            print("The roots are real and distinct.")
            r1=(-b-sqrt(d))/(2*a)
            r2=(-b+sqrt(d))/(2*a)
            print("The roots of given equation {}x^2+{}x+{} are {} and {} ".format(a,b,c,r1,r2))

        elif(d==0) :
            print("The roots are real and equal ")
            r1=-b/(2*a)
            r2=-b/(2*a)
            print("The roots of given equation {}x^2+{}x+{} are {} and {} ".format(a,b,c,r1,r2))

        else :
            print("The roots are imaginary ")
            d=-d
            r1=(-b-sqrt(d))/(2*a)
            r2=(-b+sqrt(d))/(2*a)
            print("The roots of given equation {}x^2+{}x+{} are {} and {} ".format(a,b,c,r1,r2))

elif(a==0):
    print("This becomes the linear equation and has only one solution ")
    r1=-c/b
    print("The roots of given equation {}x+{} are {}".format(b,c,r1))

else :
    print("Invalid co-efficient")




        

