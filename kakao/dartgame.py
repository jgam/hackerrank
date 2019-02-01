#dart game

#SDT (is the power number)
#options = * and #

#this is a string manipulation
#the score is from 0 to 10
#bonus is one of [S,D,T]
#option is one of [*,#, '']


def dart_game(input_string):
	#divide string into a number
	score = 0
	prev_score = 0
	current_score = 0
	power_num = 0
	power_dict = {'S':1, 'D':2, 'T':3}
	options = ['*', '#']
	option = '1'
	first_cond = True

	def comput_score(score,prev_score,adding_score, power_num, option):
		current_score = adding_score ** power_num
		if option in options:
			if option == '*':
				current_score *= 2
				score += prev_score
			else:
				current_score *= -1
		prev_score = current_score
		score += current_score
		return prev_score, score

	for i in range(len(input_string)):
		print(i)
		if input_string[i].isdigit():
			if first_cond!=True:
				'''
				current_score = adding_score ** power_num
				print('current_score is ',current_score)
				if option in options:
					#do options
					if option == '*':
						current_score *= 2
						score += prev_score
					else:
						current_score *= -1
				prev_score = current_score
				score += current_score
				'''
				prev_score, score = comput_score(score, prev_score, adding_score, power_num, option)
			adding_score = int(input_string[i])

			if input_string[i] == '0':
				adding_score = 10

		elif input_string[i].isalpha():
			if i == len(input_string) - 1:
				power_num = power_dict[input_string[i]]
				prev_score, score = comput_score(score, prev_score, adding_score, power_num, option)
			power_num =  power_dict[input_string[i]]
			first_cond = False

		else:
			option = input_string[i]
			if i == len(input_string) - 1:
				
				prev_score, score = comput_score(score, prev_score, adding_score, power_num, option)

			first_cond = False
	return score

print(dart_game('1S2D*3T'))