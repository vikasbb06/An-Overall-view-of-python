liste=[]
n=int(input("Enter The Number Of Elements In The List: "))
for i in range(n):
    ele=input(f"The {i+1} name is :") 
    liste.append(ele)
    m=int(input(f" the {i+1} student's age is :"))
    liste.append(m)

upper_list=[name.upper() for name in liste if type(name)=='str']
print(upper_list)
sub_list=[age for age in liste if type(age)=='int' and age>18]
print(sub_list)
age_list=[]
for age in liste:
    if type(age)=='int' and age>18:
        age_list.append(age)
print(age_list)
reversed_list=liste[::-1]
print(reversed_list)
reversed_list2=list(reversed(liste))
print(reversed_list2)
new_list=liste.copy()
new_list.reverse()
print("They are equal") if new_list==liste else print("They are not equal")

        





