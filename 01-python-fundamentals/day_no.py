import random
day_of_week=["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
day=int(input("The Day Number is:"))
print(day_of_week[day-1])
# print(len(day_of_week))
# print(len(day_of_week[day-1]))
tup=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,11,16,17,18,19,20)
print(tup.index(10)+1)
n=random.randint(1,1000) # another way to generate random number is random.randrange(1,1000)
p=int(input("Enter a number to check if it is the same as the random number:"))
print("Correct Guess") if n==p else print("Wrong Guess The number is ",n)





