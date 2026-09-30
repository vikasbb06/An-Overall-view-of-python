import mean
def fib(n):
    if(n==0 or n==1):
        return n
    else:
        return fib(n-1)+fib(n-2)

def main():
    try:   #exception handling for invalid input
        n=int(input("The Length of The Fibbociance series Is :"))
    except ValueError:
        print("Please enter a valid integer.")
        return
    for i in range(0,n):
        print(fib(i),end="\t")
    print("\n")
    # using another method to print the fibbocine series 
    p,q=0,1
    i=0
    for i in range(n):
        print(p, end="\t")
        # Update p and q simultaneously
        # p becomes the old q, and q becomes the sum of the two
        p, q = q, p + q
        i+=1
    print("correct sequence") if p==fib(n) else print("wrong sequence")
if __name__ == "__main__":
    if mean.mean==0:
            print("Pleae caluclate the mean first ")
            exit() 
    else:
        main()
        

    
