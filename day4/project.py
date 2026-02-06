import random
rock="""
                _______
            ---'   ____)
                  (_____)
                  (_____)
                  (____)
            ---.__(___)
            """
paper ="""
                 _______
            ---'    ____)____
                       ______)
                      _______)
                     _______)
            ---.__________)
            """
            
scissors= """
                _______
            ---'   ____)____
                      ______)
                   __________)
                  (____)
            ---.__(___)
    """

list_opt=[rock,paper,scissors]
while True:
    computer_choice =  random.randint(0,2)
    userinput = int(input("enter you choice: 0 for rock, 1 for paper and 2 for Scissors"))

    if (computer_choice ==0 and userinput ==2 ) or (computer_choice==1 and userinput==0) or (computer_choice==2 and userinput==1):
        #
        print(list_opt[computer_choice])
        print("Computer Choice")
        print(list_opt[userinput])
        print("U Lose")

    elif ((computer_choice==0 and userinput==1)  or (computer_choice==1 and userinput==2) or (computer_choice ==2 and userinput ==0 )   ):
        print(list_opt[computer_choice])
        print("Computer Choice")
        print(list_opt[userinput])
        print("U Win")
    else:

        print("Draw")
        print(list_opt[computer_choice])
        print("Computer Choice")
        print(list_opt[userinput])
        print("Try again")

        