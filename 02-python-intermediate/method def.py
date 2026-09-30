def add(a,b,n):
    match n:
        case 1:
            print("SUM is ",a+b)

        case 2:
            print("DIFFERENCE is ",a-b)

        case 3:
            print("PRODUCT is",a*b)

        case 4:
            if(a==0 or b==0):
                print("Divsion Is Not Posible")

            else :
                print("QUOTIENT is ",a/b)

try:
    a,b=map(float,input("The First,Second Number Is ").split())
    n=int(input("Enter \n 1-Add\n 2-Subtract \n 3- Multiply \n 4-Division \n"))
    add(a,b,n)
except ValueError as e:
    print("Invalid input Error occured")
