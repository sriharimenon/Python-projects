#Blackjack Tests
#Srihari Menon

import unittest
from blackjack import *



class testblackjack(unittest.TestCase):
    
    
    def test_get_card_value(self):
        self.assertEqual(get_card_value("J"),10)
        self.assertEqual(get_card_value("Q"),10)
        self.assertEqual(get_card_value("K"),10)
        self.assertEqual(get_card_value("2"),2)
        self.assertEqual(get_card_value("3"),3)
        self.assertEqual(get_card_value("4"),4)
        self.assertEqual(get_card_value("5"),5)
        self.assertEqual(get_card_value("6"),6)
        self.assertEqual(get_card_value("7"),7)
        self.assertEqual(get_card_value("8"),8)
        self.assertEqual(get_card_value("9"),9)
        self.assertEqual(get_card_value("10"),10)
        self.assertEqual(get_card_value("A"),1)

        
        self.assertNotEqual(get_card_value("100"),100)

    def test_is_ace(self):
        self.assertEqual(is_ace("A"),True)
        self.assertFalse(is_ace("J"),False)
        self.assertFalse(is_ace("Q"),False)
        self.assertFalse(is_ace("K"),False)
        self.assertFalse(is_ace("2"),False)
        self.assertFalse(is_ace("10"),False)
        self.assertEqual(is_ace("A"),True)
        self.assertEqual(is_ace("J"),False)
        self.assertEqual(is_ace("Q"),False)
        self.assertEqual(is_ace("K"),False)
        self.assertEqual(is_ace("2"),False)
        self.assertEqual(is_ace("10"),False)
        


    def test_score_hand_soft(self):
        self.assertEqual(score_hand_soft(["A"]),11)
        self.assertEqual(score_hand_soft(["A","A"]),12)
        self.assertEqual(score_hand_soft(["A","A","A"]),13)
        self.assertEqual(score_hand_soft(["A","A","A","A"]),14)
        self.assertEqual(score_hand_soft(["A","A","A","A","2"]),16)
        self.assertEqual(score_hand_soft(["A","A","A","A","K"]),24)
        self.assertEqual(score_hand_soft([]),0)
        
        
        self.assertEqual(score_hand_soft(["A","A"]),12)
        self.assertEqual(score_hand_soft(["A","2"]),13)
        self.assertEqual(score_hand_soft(["A","10"]),21)
        self.assertEqual(score_hand_soft(["A","J"]),21)
        self.assertEqual(score_hand_soft(["J","A"]),21)
        self.assertEqual(score_hand_soft(["2","2"]),4)
        self.assertEqual(score_hand_soft(["J","J"]),20)
        self.assertEqual(score_hand_soft(["Q","J"]),20)
        self.assertEqual(score_hand_soft(["J","K"]),20)

        self.assertEqual(score_hand_soft(["A","2","A"]),14)

        self.assertEqual(score_hand_soft(["2","2","2"]),6)

        self.assertTrue(score_hand_soft(["A","A"]),12)
        

    def test_score_hand(self):
        self.assertEqual(score_hand(["A"]),1)
        self.assertEqual(score_hand(["A","A"]),2)
        self.assertEqual(score_hand(["A","A","A"]),3)
        self.assertEqual(score_hand(["A","A","A","A"]),4)
        self.assertEqual(score_hand([]),0)

        self.assertEqual(score_hand(["A","A","A","A","2"]),6)
        self.assertEqual(score_hand(["A","A","A","A","K"]),14)
        self.assertEqual(score_hand(["A","A","A","A","A"]),5)

    def test_score_hand_best(self):
        
        self.assertEqual(score_hand_best([]),0)
        self.assertEqual(score_hand_best(["A"]),11)
        self.assertEqual(score_hand_best(["A"]),11)
        self.assertEqual(score_hand_best(["A","A"]),12)
        self.assertEqual(score_hand_best(["A","A","K"]),12)
        self.assertEqual(score_hand_best(["A","A","K","9"]),21)
        self.assertEqual(score_hand_best(["5","5","5","A","A"]),17)
        self.assertEqual(score_hand_best(["A","A","K","9","A"]),22)
        self.assertEqual(score_hand_best(["A","8","K","9","A"]),29)
        self.assertEqual(score_hand_best(["5","5","5","A","A"]),17)
        self.assertEqual(score_hand_best(["A","K","Q","J","10"]),41)
        self.assertEqual(score_hand_best(["A","A","K","9","A"]),22)
        self.assertEqual(score_hand_best(["2","3","4","5","A"]),15)
        self.assertEqual(score_hand_best(["8","3","4","5","A"]),21)
        self.assertEqual(score_hand_best(["9","3","4","5","A"]),22)
        self.assertEqual(score_hand_best(["8","3","A"]),12)
        self.assertEqual(score_hand_best(["8","4","A"]),13)
        self.assertEqual(score_hand_best(["7","3","A"]),21)
        
        self.assertNotEqual(score_hand_best(["A","A"]),22)
        self.assertNotEqual(score_hand_best(["A","J","10"]),31)

        self.assertFalse(score_hand_best([]),False)

    def test_is_bust(self):
        
        self.assertEqual(is_bust(["10","10","10"]),True)
        self.assertEqual(is_bust(["10","10","10","10"]),True)
        self.assertEqual(is_bust(["10","10","10","A"]),True)
        self.assertNotEqual(is_bust(["10","10","10"]),False)

        self.assertEqual(is_bust(["10","10","10","K","K","Q"]),True) 

    def test_dealer_showing(self):
        self.assertEqual(dealer_showing(["J","A"]),"A")
        self.assertEqual(dealer_showing(["A","J"]),"J")
        self.assertEqual(dealer_showing(["2","3"]),"3")
        self.assertEqual(dealer_showing(["Q","5"]),"5")
        self.assertEqual(dealer_showing(["J","A"]),"A")

    def test_dealer_hit(self):
        self.assertEqual(dealer_hit(["10","5"]),True)   # HIT for hard 15
        self.assertEqual(dealer_hit(["J","5"]),True)  # HIT for hard 15
        self.assertEqual(dealer_hit(["10","6"]),False)  # HIT for hard 16
        self.assertEqual(dealer_hit(["J","6"]),False)  # HIT for hard 16

        self.assertEqual(dealer_hit(["A","5"]),True) # HIT for soft 16
        self.assertEqual(dealer_hit(["10","7"]),False)
        self.assertEqual(dealer_hit(["10","10"]),False)
        

#######################################
unittest.main()
