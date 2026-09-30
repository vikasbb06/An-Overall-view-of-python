def reverse(n):
    rev_num=0
    while(n!=0):
        rev_num=rev_num*10+n%10
        n=n//10
    return rev_num

n=int(input("The Number That Is To Be Reversed Is: "))
if(n==reverse(n)):     
    print("PALINDROME")
    print("The  Number Entered is:{} \nReversed Number Is:{}".format(n,reverse(n)))
else:
    print("NOT A PALINDROME")
    print("The  Number Entered is:{} \nReversed Number Is:{}".format(n,reverse(n)))

   
    
   
