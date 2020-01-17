#probability sim
import random

numTrials = 5000000
player1WinCount = 0
player2WinCount = 0

for i in range (0,numTrials):
	p1Roll = random.randrange(100)
	p2Roll = random.randrange(100) + 30

	if (p1Roll <= p2Roll): #player 1 lost the roll
		player2WinCount += 1

	elif (p2Roll <= p1Roll):
		player1WinCount += 1

print ("After " + str(numTrials) + " trials: Player 1 won " + str(player1WinCount) + " times(" + str((player1WinCount/numTrials)*100) + "%). Player 2 won " + str(player2WinCount) + " times(" + str((player2WinCount/numTrials)*100) + "%).")

