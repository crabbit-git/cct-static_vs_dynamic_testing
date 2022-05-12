import unittest

from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):

    def setUp(self):
        self.card1 = Card("Spades", 1)
        self.card2 = Card("Hearts", 12)
        self.card3 = Card("Diamonds", 1)

    def test_card_is_ace(self):
        self.assertEqual(True, CardGame.check_for_ace(self, self.card1))

    def test_card_is_not_ace(self):
        self.assertEqual(False, CardGame.check_for_ace(self, self.card2))

    def test_high_card_returned(self):
        self.assertEqual(self.card2, CardGame.highest_card(self, self.card1, self.card2))

    def test_card_values_equal(self):
        self.assertEqual(None, CardGame.highest_card(self, self.card1, self.card3))

    def test_cards_total(self):
        cards = [self.card1, self.card2, self.card3]
        self.assertEqual("You have a total of 14", CardGame.cards_total(self, cards))
