list=["Physics","Chemistry","Sanskrit","Machine Learning","Python"]
print("Initial List is:",list)
print(list[-3:-3])
list.insert(3,"Electrical")
print("Inserted List is :",list)
list.remove("Chemistry")
print("Removed List is:",list)
print("Length Of The Array is:",len(list))
list.append("Chemistry")
print("Appended List is :",list)
list.pop()
print("Popping List is:",list)
for i in range(1,len(list),2):
    print(list[i])

list.clear()
print("List After Clear is:",list)

