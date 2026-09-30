class Student:
    College="RVITM"
    def __init__(self,phy,chem,maths):
        self.phy=phy
        self.chem=chem
        self.maths=maths
        
    @property #this is the called a property atttribute and and itchanges dynamically when-ever the attributes changes  
    def percentage(self):#this returns as a attributes as @property is called
        return str((self.phy+self.chem+self.maths)/3)+"%"
    
class MovieGoer:
    def __init__(self, name, age):
        self._name = name
        self._age = age  # The underscore means "keep hands off, use the gatekeeper!"

    # 1. THE GETTER:Lets people read the age easily, for setter property the getter must be present 
    @property
    def age(self):
        print("Checking the records...")
        return self._age
    @property
    def name(self):
        return self._name

    # 2. THE SETTER: Bouncer that checks the age before updating it
    @age.setter
    def age(self, new_age):
        print(f"Trying to change age to {new_age}...")
        if new_age < 0:
            print("🚫 Hold on! You cannot have a negative age!")
        else:
            print("✅ Age update approved.")
            self._age = new_age
    @name.setter
    def name(self,checking):
        check=checking.replace(" ","") # this is used to remove the spaces in the name
        if check.isalpha():
            print("✅ Name is valid, updating the name.")
            self._name=checking
        else:
            print("🚫 Invalid name! Names should only contain letters.")
try:
    S1=Student(98,94,95)
    print(S1.percentage)
    S1.phy=99
    print(S1.percentage) 
    customer = MovieGoer("Alice", 25)

    # Using the GETTER (Notice: No parentheses needed, looks like a normal variable)
    print(customer.age)  

    print("\n--- Attempting a bad update ---")
    # Using the SETTER to try an invalid age
    customer.age = -5 
    customer.name="M3" 
    print(customer.age,customer.name)  # Age remains 25 because the bouncer blocked -5

    print("\n--- Attempting a good update ---")
    # Using the SETTER to try a valid age
    customer.age = 20 
    customer.name="M Bhat" 
    print(customer.age,customer.name)  # Age successfully updates to 30
except ValueError:
    print("Error")
except NameError:
    print("Error")
except ValueError:
    print("Error") 