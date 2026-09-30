# problem 4
my_list=[]
try:
    while True:
        num=input("Enter the Elemnts Of the Array (Press Enter without input to stop): ")
        if num=='':
            break
        my_list.append(num)
    operation=int(input("enter \n1.Insertion\n2.Deletion\n3.Appending\n4.Length of Array\n5.Popping\n6.Clearing"))
    match operation:
        case 1:
            element=input("\nEnter the element to insert: ")
            index=int(input("\nEnter the index to insert the element:"))
            my_list.insert(index,element)
            print(f"Updated List :{my_list}")
        case 2:
            element=input("\nEnter the element to Remove:")
            try:
                my_list.remove(element)
                print(f"Updated List :{my_list}")
            except ValueError:
                print("Error :No Element Found")
        case 3:
            element=input("\nEnter the element to Appended:")
            my_list.append(element)
            print(f"Updated List :{my_list}")
        case 4:
            print(f"\n The Length Of The Array Is:{len(my_list)}")
        case 5:
            try:
                popped=my_list.pop()
                print(f"\n Popped Element :{popped}")
                print(f"Updated List :{my_list}")
            except Exception:
                print("Error :NO Element To Pop")
        case 6:
            my_list.clear()
            print(f"Updated List :{my_list}")
        case Default:
            print("Invalid Operation")
except Exception as e:
    print(f"An error occurred: {e}")



        


