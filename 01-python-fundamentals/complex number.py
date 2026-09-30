class Complex:
    def __init__(self,real,imag):
        self.imag=imag
        self.real=real

    def __str__(self):
        if self.imag>0:
            return f"{self.real} +i{self.imag}"
        else:
            return f"{self.real} -i{self.imag}"
    def add_complex(c1,c2): # we can call this method outside class also return for class to get the desired output
        return Complex(c1.real+c2.real,c1.imag+c2.imag)


print("\n Enter the complex Numbers.")
N=int(input("\n The Number Of The Complex number Is :"))
if N<2:
    print("\n Cannot be added")
    exit()
else: 
    result=Complex(0,0)
    for i in range(0,N):
        try:
            real=float(input(f"\nEnter the {i+1} real number :"))
            imag=float(input(f"\nEnter the {i+1} imaginary number :"))
            c1=Complex(real,imag) #we can create like this 
            #c1=Complex(float(input(f"\nEnter the {i+1} real number :")),float(input(f"\nEnter the {i+1} imaginary number :")))
            result=Complex.add_complex(c1,result)
        except ValueError as e:
            print(f"Error :{e}")
        except Exception as fe: 
            print(f"\nError: {fe}")
print("\n Total Sum Is:",result)

