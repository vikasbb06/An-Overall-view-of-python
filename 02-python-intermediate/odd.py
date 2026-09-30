n=int(input("The number is :"))
for i in range(n+1):
    if(i%2!=0):
        print(f"{i} is a odd number")

    else:
        print("{} is not odd number".format(i))
try:
    a,b,c=map(int,input("Enter the numbers:").split())
    large= a if a>b and a>c else b if b>c and b>a else c
    print("The largest number is ",large)
except ValueError as e:
    print("Error",e)
str1,str2,str3=(input("The Sting iS :").split())  
liste=[1,2,3,4,5]
new_liste=[i**2 for i in range(len(liste))] #this is equal to list**list or list**2
new_liste2=[]; 
# liste=liste**2 this is unsupported for list and int data types and also pow functiom
new_liste2=new_liste
print(True) if new_liste==new_liste2 else print(False)
print(new_liste)

