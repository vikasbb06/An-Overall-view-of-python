import day_no
def fact(n):
    if(n==1):
        return 1
    else :
        return n*fact(n-1)
def number(n):# this function prints the number till 0 using recursion(calling a function itself)
    print(n,end=" ")
    if n==0: #base case
        return
    else:
        return number(n-1)#recursive case of calling teh function itself

n=int(input("The Number to Find a Factorial :"))
print("FACTORIAL is ",fact(n))
number(n)
n=int(input("The number is :"))
if n==day_no.day:
    exit() 
threshold=0.1
approx=n/2
while True:
    better=(approx+n/approx)/2
    if abs(approx-better)<threshold:
        print(better)
        break
    approx=better
