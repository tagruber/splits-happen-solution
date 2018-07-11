# Bowling game simulator
# Author: Tim Gruber
# 07/11/2018

class Bowling:

	def __init__(self, rolls):
		self.rolls = rolls	

	# plays a frame
	def play(self, scoreString):

		scores = list(scoreString)
		for i in range(len(scores)):
			if scores[i] == "X":
				self.rolls[i] = 10
			elif scores[i] == "-":
				self.rolls[i] = 0
			elif scores[i] == "/":
				self.rolls[i] = 10 - self.rolls[i - 1]
			else:
				self.rolls[i] = int(scores[i])


	# scores a frame of bowling
	def score(self):	
		score = 0
		frame = 0

		for i in range(10):
			if self.rolls[frame] == 10:
				score += 10 + (self.rolls[frame + 1] + self.rolls[frame + 2])
				frame += 1
			elif((self.rolls[frame] + self.rolls[frame + 1]) == 10):
				score += (10 + self.rolls[frame + 2])
				frame += 2
			else:
				score += (self.rolls[frame] + self.rolls[frame + 1])
				frame += 2

		return score


if __name__ == '__main__':
	# runs a simulation of the game
	inScore = raw_input("Enter a valid bowling score: ")
	rolls = [None]*21
	game = Bowling(rolls)
	game.play(inScore)
	print str(game.score())


	
