#CONTEXT
#Game of Blackjack

#functions, list collection, Test-driven-developemnt

import random


#global deck
#deck = ['2','2','2','2','3','3','3','3','4','4','4','4','5','5','5','5','6','6','6','6','7','7','7','7','8','8','8','8','9','9','9','9','10','10','10','10','J','J','J','J','Q','Q','Q','Q','K','K','K','K','A','A','A','A']
##global J
##J = 10
##global Q
##Q = 10
##global K
##K = 10
##global A
##A = 1 ####### or 11

##############################################
#Write each of these functions as specified.
#You must use test driven development for all
#Functions in this section.
##############################################

def get_card_value(s):
    """Get the integer points for the card "s".
    2-10 = int value; J,Q,K = 10; A = 1

    Inputs:
    s (string) - string value of card

    Output:
    return (int) the score of the card

    Exception:
    If s doesn't match to any cards, raise ValueError"""
    ####################################################
    card_score = 0
    if (s == "J" or s=="Q" or s=="K"):
        
        card_score = 10
        
    elif s == "A":
        
        card_score = 1

        
    elif (int(s) >= 1 and int(s) <= 10):
        card_score = int(s)
    else:
        print("This is a ValueError! It is an integer outside of the deck values!")
        card_score = 0
        
    return (card_score)
  
  
def is_ace(card):
    """Returns (boolean) True if card is an ace.
    Returns (boolean) False otherwise

    Inputs:
    Card - a string representing card value

    Outputs:
    boolean - True/False if card is an ace"""
    ####################################################
    if card == "A":
        return(True)
    else:
        return(False)
    

def score_hand_soft(hand):
    """Score hand assuming the first ace (if any) is worth 11.
    All other aces after the first (if any) are worth 1.
    
    Inputs:
    hand - a list of strings, each string representing a card.
    Example input: ["A","J"] - this would output 21

    Outputs:
    Returns an integer score.
    0 points if hand is empty."""

    hand_score = 0


    if(hand.count("A")):
       hand_score=hand_score+10
    
    for i in range(0,len(hand)):
        hand_score = hand_score + get_card_value(hand[i])

    
    return(hand_score)


def score_hand(hand):
    """Score the hand assuming all aces (if any) are worht 1.

    Inputs:
    hand - a list of strings, each string representing a card.
    Example input: ["A","J"] - this would output 11

    Outputs:
    Returns an integer score.
    0 points if hand is empty."""
    ####################################################

    hand_score = 0
    
    for i in range(0,len(hand)):
        hand_score = hand_score + get_card_value(hand[i])

    return(hand_score)
    


    

def score_hand_best(hand):
    """Return the best score. That is the larger score between
    score_hand and score_hand_soft that is less than 21. If both
    scores are greater than 21, return the smaller number

    Inputs:
    hand - a list of strings, each string representing a card.
    Example input: ["A","J"] - this would output 21
    Example input: ["A", "J", "10"] - this would output 21

    Outputs:
    Returns an integer score.
    0 points if hand is empty."""
    ####################################################

    if score_hand(hand) == score_hand_soft(hand):
        return (score_hand(hand))
    
    if score_hand(hand) > score_hand_soft(hand):
        if score_hand(hand) > 21:
            return (score_hand_soft(hand))
        else:
            return (score_hand(hand))

    if score_hand(hand) < score_hand_soft(hand):
        if score_hand_soft(hand) > 21:
            return (score_hand(hand))
        else:
            return (score_hand_soft(hand))
        
       
def is_bust(hand):
    """Returns true if hand is bust. A hand is bust if the best
    score is over 21.
    Inputs:
    hand - a list of strings, each string representing a card.

    Outputs:
    Returns True/False whether or not hand is bust."""
    ####################################################
    if score_hand(hand) > 21 and score_hand_soft(hand) > 21:
        return (True)
    else:
        return (False)
        

def dealer_showing(hand):
    """The dealer hides one card face down until their turn.
    As such, this method should return only one card.
    Specifically, return the second card.
    Example: hand = "J","A", only show "A".

    Inputs:
    hand - a list of strings, each string representing a card.
    As a precondition, you can assume this function is only
    called when the dealer has 2 cards in their hand.

    Outputs:
    Returns (string) the second card in the dealer's hand."""
    ####################################################

    return(hand[1])

def dealer_hit(hand):
    """Returns True if the dealer would hit. A dealer hits
    on SOFT 16, of 15 or less. The dealer does not hit on
    HARD 16, or on 17 and above.
    Inputs:
    hand - a list of strings, each string representing a card.

    Outputs:
    Returns True if the dealer would hit.
    Returns False if the dealer would stand."""
    ####################################################


    if score_hand(hand) >= 16:
        return (False)
    else:
        return (True)

    if hand_score_soft(hand) <= 16:
        return (True)
    else:
        return (False)
    


def get_deck():
    """Returns a "deck" of cards as a list. The list looks like:
    ["2","2","2","2","3","3","3","3",..."A","A","A","A"]
    4 of each card 2 through 10, J, Q, K, A.
    Try to do this somewhat procedurally rather than
    typing everything out.
    Order of cards in the deck doesn't matter.
    You do not need to shuffle the deck in this function.

    Inputs: None

    Outputs: A deck of 52 cards."""
    ####################################################
    
#    deck = ['2','2','2','2','3','3','3','3','4','4','4','4','5','5','5','5','6','6','6','6','7','7','7','7','8','8','8','8','9','9','9','9','10','10','10','10','J','J','J','J','Q','Q','Q','Q','K','K','K','K','A','A','A','A']

    deck = []

    for card in range(2,11):
        for counter in range(1,5):
            deck.append(str(card))

    for card in ("J", "Q", "K", "A"):
        for counter in range(1,5):
            deck.append(str(card))  # string is extra here but still works...would work anyways because it is already multiplying strings.

    return(deck)



def shuffle_deck(deck):
    """Shuffles the deck. Use random.shuffle(list)
    Inputs: a deck of cards, represented as a list of strings.

    Outputs: Doesn't explicityly return anything.
    Note that random.shuffle is DESTRUCTIVE (buzzword from class).
    """
    ####################################################
#    deck = ['2','2','2','2','3','3','3','3','4','4','4','4','5','5','5','5','6','6','6','6','7','7','7','7','8','8','8','8','9','9','9','9','10','10','10','10','J','J','J','J','Q','Q','Q','Q','K','K','K','K','A','A','A','A']

    
    random.shuffle(deck)


def draw_card(deck):
    """Remove the first card on the deck and return it.
    Use list.pop()

    Inputs: a deck of cards, represented as a list of strings.

    Outputs: Returns the card removed from the deck.
    Note that list.pop is DESTRUCTIVE (buzzword from class).
    Do NOT return the deck itself. Only the card removed.
    """
    ####################################################

    return(deck.pop(0))


def hit_me():
    """Prompt the user to hit or stand.
    If the user enters a word starting with H/h, return true
    If the user enters a word starting with S/s, return false
    If anything else, prompt again:

    Inputs: None
    
    Outputs: True if the human player hits. False if they
    stand."""

### Infinite loop here to make sure there is something that is accepted being chosen. VERY DANGEROUS BUT ONLY SIMPLE OPTION! 
    while True:
    
        entry = input("Do you want to (H)it or (S)tand? ")
    ####################################################
        if entry[0] == "H" or entry[0] == "h":
            return(True)
        elif entry[0] == "S" or entry[0] =="s":
            return(False)
        else:
            print("invalid entry")
        
        


def play_hand():
    """Plays a round of Blackjack. This function should
    not be changed. If your functions work correctly, this
    will work as well.
    Returns True if you win
    Returns False if you lose"""
    
    #create deck
    deck = get_deck()

    #shuffle the deck
    shuffle_deck(deck)

    #create empty hands
    human_hand = []
    dealer_hand = []

    #Each player gets 2 cards
    human_hand.append(draw_card(deck))
    dealer_hand.append(draw_card(deck))
    human_hand.append(draw_card(deck))
    dealer_hand.append(draw_card(deck))

    #Print status
    print("You have", human_hand)
    print("The dealer is showing", dealer_showing(dealer_hand))

    #If you have blackjack, you win
    if(score_hand_soft(human_hand) == 21):
        print("Blackjack!")
        return True

    #Hitting loop
    still_hitting = True
    while still_hitting and len(human_hand) < 5:
        print("You have", human_hand)
        
        #Prompt for hit or stand
        if hit_me(): #If Hit
            #Draw a card
            card = draw_card(deck)
            print("You drew", card)
            human_hand.append(card)

            #If you bust, you lose
            if is_bust(human_hand):
                print("Oh no! Bust!", human_hand)
                return False
        else: #If stand
            still_hitting = False


    #Check if you already lost
    if score_hand_best(dealer_hand) > score_hand_best(human_hand):
        print("Oh no! The dealer won!")
        return False;  


    #begin dealer turn
    while dealer_hit(dealer_hand) and len(dealer_hand) < 5:
        #draw a card
        card = draw_card(deck)
        print("Dealer drew",card)
        dealer_hand.append(card)
        
        #bust check
        if is_bust(dealer_hand):
            print("Yes! Dealer busts!", dealer_hand)
            return True
        
        #beat human check
        if score_hand_best(dealer_hand) > score_hand_best(human_hand):
            #dealer has better hand than human
            #Stop drawing
            break
    print("Your hand", human_hand)
    print("Dealer hand", dealer_hand)
    if score_hand_best(dealer_hand) > score_hand_best(human_hand):
        print("Oh no! The dealer won!")
        return False
    elif score_hand_best(dealer_hand) == score_hand_best(human_hand):
        print("Push! It's a tie!")
        return False #Not the same as winning
    else:
        print("Congratulations! You win!")
        return True


def main():
    while True:
        print("Starting a new game. Close the window to stop playing.")
        print("")
        input("Press enter to continue")
        play_hand();

if __name__ == "__main__":
    main();
