#CONTEXT
#"Pig" is a very simple game. Two players take turns; on each turn, a player rolls a six-sided die
#("die" is the singular of "dice") as many times as she wishes, or until she rolls a 6. Each number
#she rolls, except a 6, is added to her score this turn; but if she rolls a 6, her score for this turn is
#zero, and her turn ends. At the end of each turn, the score for that turn is added to the player's
#total score. The first player to reach or exceed 50 wins.

#functions

#Srihari Menon


#####################################################################################################################################################################
# Section 1: Main Program
#####################################################################################################################################################################


def instructions():
    """These are simply the printed instructions as I have understood them for the game."""
    print("""
(***In Hannibal Lecter voice***) HELLO, Clarice!!!

You are about to play PIG. This is a game to battle the computer in a game of chance to a certain number. GOOD LUCK
""")
    print("1. These are the following rules of the game...")
    print("2. Player_1(The Computer) goes first, always.")
    print("3. Player_2(The User) is a human player and they go second.")
    print("4. The Die options are 1, 2, 3, 4, 5, and 6.")
    print("5. Rolling a '6' will end your turn and result in a score of 0 for that turn.")
    print("6. If you end your turn before rolling a 1, then your scores from each turn are added together toward your total [trying for 50]")
    print("7. If Player_1 gets 50 or better FIRST...then Player_2 gets 1 additional turn.")
    print("8. If Player_2 gets 50 or better FIRST...then Player_1 loses and gets no additional turns.")
    print("9. If Player_1 AND Player_2 TIE with 50 or more...then each player will get one more additional turn until the tie is broken.")
    print("                                                                                         ")
    print("""(In Jigsaw voice)I WANNA PLAY A GAME!

Game Begins HERE!!!
--------------------------------------------------------------------------------------------------------------------------------------------------------------------""")
    print("                                                                                         ")

############################################################################################################################################################################
############################################################################################################################################################################
def ask_yes_or_no(prompt):
    """This function is the defining prompt of when to ask for the choice of deciding to continue guessing or call it quits for the round. This is ONLY for the user."""
    choice = input(prompt)
    if choice == "y":
        return(True)
    elif choice == "n":
        return(False)
    else:
        while choice != "y" or choice != "n":
            choice = input(prompt)
            if choice == "y":
                return(True)
            elif choice == "n":
                return(False)
        
############################################################################################################################################################################
############################################################################################################################################################################        
    

def roll():
    """This section is calling the random module from the Python website. It is setting up the possible rolls of a die for the game."""
    import random
    dieroll = random.randint(1,6)
    return(dieroll)

############################################################################################################################################################################
############################################################################################################################################################################

def human_move(computer_score, human_score):
    """This is the setup for the human user. It prints the currents scores then goes into rolling for the current move. It incorporates a while loop with a nested if-else statment. It also controls the case of if the user rolls a '1'."""

    print("current computer score",computer_score)
    print("current human score",human_score)
    print("current difference",abs(computer_score - human_score),"""

""")
    
    Restart = True
    
    temp_score=0    

    while Restart:

        dieroll=roll()

# This portion dictates what rolls are allowed. I am using an if-else loop and "!=" not equals value here to remove the die roll of 6. So now, rolls 1-5 are allowed and summed.
# Here, and other places, I use "temp_score" to add up the rolls of the die...at least until the turn is ended (whether from the roll of a 6 or by the user).
        if dieroll != 6: #roll = 1, 2, 3, 4, or 5.
            print("Good roll!", "You got a ",dieroll)
            temp_score = temp_score + dieroll
            Restart = ask_yes_or_no("""Do you want to roll again(y/n)?
""")
        else:
             print("""
turn over! you rolled a """,dieroll,"""!!!!!!
""")
             temp_score=0
             Restart = False


    human_score=human_score+temp_score

    return(human_score)


############################################################################################################################################################################
############################################################################################################################################################################


def computer_move(computer_score, human_score):
    """The computer move section is set to be intelligent. It rolls a random amount of 1-3 turns if ahead and random number between 4-6 if behind. It also uses an index to add the number of times the loop has been run because it is not meant to roll more than 3x if ahead or 6x if behind."""

    comp_roll = 0

    temp_score = 0
    max_roll=0

    import random
    
    if computer_score >= human_score:
        max_roll=random.randint(1,3)
    else:
        max_roll=random.randint(4,6)

    i=0
##i is a counter index. We also saw another means in office hours using the += format for recursion.

    while comp_roll != 6 and  i<max_roll:

        comp_roll = roll()
        print("computer rolls ",comp_roll)


        if comp_roll!=6:
            temp_score = temp_score + comp_roll
        else:
            temp_score=0
            print("""Player 1 (The Computer) rolled a 6 and their turn is over
""")

        i=i+1


    computer_score=computer_score+temp_score
        

    return(computer_score)


############################################################################################################################################################################
############################################################################################################################################################################


def is_game_over(computer_score, human_score):
    """This controls whether or not the game is to continue after the human user's move. It's really about that simple. Uses two if-else statements with one nested."""
    if computer_score >= 50 or human_score >= 50:
        if computer_score != human_score:
            return(True)
        else:
            return(False)
    else:
         return(False)


############################################################################################################################################################################
############################################################################################################################################################################
    

def show_results(computer_score, human_score):
    """This is describing whether the human user won or lost the game and the amount. Uses an if-elif statement."""
    if computer_score > human_score:
        print("Player_1 (The Computer) wins")

    elif human_score > computer_score:
        print("Congratulations! Player_2 (The Human User) wins!")

    print("They won by",abs(computer_score - human_score), "points and it made all the difference...","""
""")

    dummy=input("press any key to end")
        

############################################################################################################################################################################
############################################################################################################################################################################
        


def main():
    """The main function from where the program executions occur. I realized that we can define them in any order more or less as long as we call them in main correctly.
There is a Piazza post about when "main()" will prove problematic and I hope we can discuss this somewhat in class or OHs to clarify the import/testing cases."""
    instructions()
    computer_score = 0
    human_score = 0
    while not (is_game_over(computer_score, human_score)):
        
        computer_score = computer_move(computer_score, human_score)
        human_score = human_move(computer_score, human_score)

    show_results(computer_score, human_score)
    


main()


############################################################################################################################################################################
############################################################################################################################################################################



#####################################################################################################################################################################
# End Code
#####################################################################################################################################################################
