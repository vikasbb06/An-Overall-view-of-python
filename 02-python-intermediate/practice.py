import string
name="Vikas" #string
age=20
price=25.99
print(f"{name} is my name") 
info={
    "name": "Vikas",    #key:value pair separated by comma
    "age": 20,
    "price": 25.99, "is_adult":True,
    20:"age in number"
    }
print(info)
print(type(list))
print(info["age"]) #accessing value using key
print(info.get("name")) #accessing value using get method
print(info.get(20))
info["age"]="Ningyko nanna age" #updating value using key & it's overwrite the old value
print(info.get("age"))
details={
    "name":"tirupathi",
    "subjects":{        #nested dictionary
        "physics":90,
        "chemistry":95,
        "maths":98
    }
}
liste=list(details.keys())
for ch in liste:
    print(ch)
print(details["subjects"]["maths"])
details["subjects"]["physics"]= 50
print(details.get("subjects").get("physics"))
# #details.update({"subjects":{"physics":0}}) updating value using update method and its update the whole nested dictionary
# # print(details.get("subjects").get("physics"))
# # print(len(details))
print(len(details["subjects"]))
print(details.items()) #returns a list of tuples containing key-value pairs
print(details.values()) #returns a list of all the values in the dictionary 
details.update({"Class":"2nd sem engineering"})
print(details)
str="Hello, World! and python program #*$"
str2="".join(ch for ch in str if ch not in string.punctuation)
print(str2)
