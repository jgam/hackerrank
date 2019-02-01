#dartgame2
def compute(equation):
	num = 0
	prev_twice = False
	operation = 0
	power_num = 0
	operation_list = ['*', '#']
	math_list = {'S':1, 'D':2, 'T':3}
	for i in range(len(equation)):
		if equation[i].isdigit():
			if equation[i] =='0' and equation[i-1]=='1':
				num = 10
				continue
			num = int(equation[i])
			continue

		if equation[i].isalpha():
			power_num = math_list[equation[i]]
			num = num ** power_num
			#print(num)
			continue
		if equation[i] in operation_list:
			if equation[i] == '*':
				prev_twice = True
				num *= 2
			elif equation[i] == '#':
				num *= -1
			else:
				continue
	return prev_twice, num



def dart_game(input_string):
	#first reduce the string into a list
	#then each list run the functiuon and get the sum at the end
	ret_score = 0
	ret_list = []
	input_list = []
	ten_cond = False
	string_code = ''
	for i in range(len(input_string)):
		if i == 0:
			string_code += input_string[i]
			continue

		if input_string[i].isdigit():
			if input_string[i+1]=='0':
				ten_cond = True
				continue
			input_list.append(string_code)
			string_code = ''

		string_code += input_string[i]
		
		if ten_cond:
			string_code = '10'
			ten_cond = False

		if i == len(input_string) - 1:
			input_list.append(string_code)

	for i in range(len(input_list)):
		if i ==0:
			previous, score = compute(input_list[i])
			ret_list.append(int(score))
			continue


		previous, score = compute(input_list[i])
		if previous:
			ret_list[i-1] = ret_list[i-1]*2
		ret_list.append(score)
	#print(ret_list)
	return sum(ret_list)
		#compute each element
inputtts = ['1S2D*3T', '1D2S#10S', '1D2S0T', '1S*2T*3S', '1D#2S*3S', '1T2D3D#', '1D2S3T*']
for i in inputtts:
	print(dart_game(i))