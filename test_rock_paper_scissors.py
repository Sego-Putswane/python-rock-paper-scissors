import unittest
from rock_paper_scissors import get_player_name

class TestRockPaperScissors(unittest.TestCase):
    def test_get_player_name(self):
        player_name = "Sego" 
        self.assertEqual("Welcome to Rock, Paper Scissors, sego")