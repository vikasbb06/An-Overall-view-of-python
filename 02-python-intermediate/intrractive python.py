game_list=[0,1,2]

def display_game(game_list):
    print("The game list is :")
    print(game_list)

def position_choice():
    choice="wrong"
    while choice not in ['0','1','2']:
        choice=input("The position is (0,1,2):")

        if choice not in ['0','1','2']:
            print("Invalid Position")

    return int(choice)

def replacement(game_list,position):
    replace=input("The string to be replace in the given position is:")
    game_list[position]=replace
    print("Updated game List is",game_list)
    

def continue_play():
    choice="wrong"
    while choice not in ['Y','N']:
        choice=input("Do You Want You to Continue To Play (Y or N)?")
        choice=choice.upper()
        if choice not in ['Y','N']:
            print("inavlid Answer!")
    return(choice)
       

def main():
    print("Welcome to the inter-active pyhton piece of code")
    condition=True
    while condition:
        display_game(game_list)
        replacement(game_list,position_choice())
        choice=continue_play()
        if choice!="Y":
            condition=False
        else:
            condition=True
            
if __name__=="__main__":
    main()





    





