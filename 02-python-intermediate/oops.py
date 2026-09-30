class student:
    college="RVITM Bangalore" # class variable or attributes
    def __init__(self,name,rollno):
        self.name=name # by deafult it is public attributes
        self.__rollno=rollno # this is the private attributes and
        #it can be accessed onlly within the class 
    def __roll(self):
        print("roll no from private attributes:")
    @classmethod
    def change_college(cls,new_college):
        cls.college=new_college # this is used to change the class variable or attributes &cls is keyword         
    def display(self):    
        print("name:",self.name)
        print("rollno:",self.__rollno)
        self.__roll()  #like this we can call the private method and attributes
class teacher(student): #this is inheritance teacher=child class & student=parent class
    def __init__(self,name,rollno,subject): 
        super().__init__(name,rollno) # this is used to call the parent class constructor
        self.subject=subject 
    def display(self):
        super().display() # this is used to call the parent class method
        print("subject:",self.subject)

        
S1=student("Vikas Bhat","1RF25CS175") 
print(S1)
print(S1.display())
#print(S1.teacher) this will give error because teacher is not a attribute of student class
S1=teacher("vikas bhat","1RF25CS175","python") # this is the object of teacher class 
#but it can access the student class attributes and methods because of inheritance
print(S1)
print(S1.display()) 
S2=student("Vinod","1RF25CS179")
print(S2)
print(S2.display())
op=input("Enter the student who left the school:")
if op.lower()=="vikas bhat":
    del S1
    print("Record Deleted Succesfully")
elif op.lower()=="vinod":
    del S2
    print("Record Deleted Succesfully")
else:
    print("No student in the Records")   