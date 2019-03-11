#숫자야구

#while loop

player1 = input("put your name\n")
player2 = input("put your name, you are the second player\n")

#print("welcome to the cos and bulls game")

p1_num = str(input("put your number "+player1+" (4digits only)\n"))
for i in range(100):
	print("****")

if len(p1_num) != 4:
	print('input carefully... you are smarter than that')

p2_num = str(input("put your number, "+ player2 + " (4digits only)\n"))

for i in range(100):
	print("****")

if len(p2_num) != 4:
	print('input carefully... you are smarter than that')

p1_history = {}
p2_history = {}
while True:
	if len(p1_history) == 0:
		print("you have no history player 1")
	else:
		print('\n\n')
		print(player1 + "\'s history of guessed numbers are the following:\n")
		print(p1_history)
	p1_guess = str(input("player 1, guess the number(4digits only)\n"))

	#now check the input and guessed number
	strike_num = 0
	ball_num = 0
	out_num = 0
	
	for character in p1_guess:
		if character in p2_num:
			try:
				v = p2_num.index(character)
				if p1_guess.index(character) == v:
					strike_num += 1
				else:
					ball_um += 1
			except:
				ball_num += 1
		else:
			out_num += 1
	p1_history[p1_guess] = str(strike_num) + ' s ' + str(ball_num) + ' b ' + str(out_num) + ' o'
	p1_strike_num = strike_num 
	strike_num = 0
	ball_num = 0
	out_num = 0
	#here is the second case
	if len(p2_history) == 0:
		print("you have no history player 2")
	else:
		print('\n\n')
		print(player2+"\'s history of guessed numbers are the following:\n")
		print(p2_history)

	p2_guess = str(input("player 2, guess the number(4digits only)\n"))

	for character in p2_guess:
		if character in p1_num:
			try:
				v = p1_num.index(character)
				if p2_guess.index(character) == v:
					strike_num += 1
				else:
					ball_num += 1
			except:
				ball_num += 1
		else:
			out_num += 1

	p2_history[p2_guess] = str(strike_num) + ' s ' + str(ball_num) + ' b ' + str(out_num) + ' o'
	p2_strike_num = strike_num
	if p1_strike_num == 4:
		if p2_strike_num == 4:
			print('Tie')
			break
		else:
			print(player1 + ' won!')
			break
	elif p2_strike_num ==4:
		print(player2 + ' won!')
		break
	else:
		continue

