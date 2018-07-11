#unit tests

import unittest
from bowling import *

class TestBowling(unittest.TestCase):
	
	def setUp(self):
		self.rolls = [None]*21
		self.game = Bowling(self.rolls)
		
	def testStrikes(self):
		gameTest = "XXXXXXXXXXXX"
				
		self.game.play(gameTest)

		self.assertEqual(self.game.score(), 300)

	def testSpares(self):
		gameTest = "5/5/5/5/5/5/5/5/5/5/5"
		self.game.play(gameTest)
		
		self.assertEqual(self.game.score(), 150)

	def testMiss(self):
		gameTest = "9-9-9-9-9-9-9-9-9-9-"
		self.game.play(gameTest)

		self.assertEqual(self.game.score(), 90)

	def testMix(self):
		gameTest = "X7/9-X-88/-6XXX81"
		self.game.play(gameTest)

		self.assertEqual(self.game.score(), 167)

	def testGameFail(self):
		gameTest = "x"
		with self.assertRaises(ValueError):
			self.game.play(gameTest)
			self.game.score()

if __name__ == '__main__':
	unittest.main()


