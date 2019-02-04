#news clustering

#multiply 65536
def news_clustering(one, two):
	one_list = []
	two_list = []
	common = 0
	total = 0
	'''
	real_one = ''
	real_two = ''
	for i in one:
		if i.isalpha():
			real_one+=i
		else:
			continue
	for i in two:
		if i.isalpha():
			real_two+=i
		else:
			continue

	one = real_one
	two = real_two
	'''
	#-2 because the size of string is 2
	#one_list = [one[i-2:i] for i in range(2, len(one))]
	#one_list.append(one[len(one)-2:])
	for i in range(2, len(one)):
		v = one[i-2:i].lower()
		if one[i-2].isalpha() and one[i-1].isalpha():
			one_list.append(v)
		else:
			continue

	v = one[len(one)-2:].lower()
	if one[len(one)-2].isalpha() and one[len(one)-1].isalpha():
		one_list.append(v)
	#two_list = [two[i-2:i]if two[i].isalpha() and two[i-1].isalpha() else '' for i in range(2, len(two))]
	#two_list.append(two[len(two)-2:])
	for i in range(2, len(two)):
		v = two[i-2:i].lower()
		if two[i-2].isalpha() and two[i-1].isalpha():
			two_list.append(v)
			print('forming two_list : ', v, two[i-2:i])
			if v in one_list:
				print(two[i-2:i])
				common += 1
				total -= 1
		else:
			continue
	v = two[len(two)-2:].lower()
	if two[len(two)-2].isalpha() and two[len(two)-1].isalpha():
		two_list.append(v)
		if two[len(two)-2:len(two)].lower() in one_list:
			print(two[i-2:i])
			common += 1
			total -= 1

	total += len(one_list)
	total += len(two_list)
	if total==0 or common/total == 0:
		return 65536
	elif common == len(two_list):
		return int(65536*(min(len(one_list), len(two_list))/ max(len(one_list), len(two_list))))
	else:
		return int(65536 * (common/total))

	
	#

#str1 = 'FRANCE'
#str2 = 'french'
#answer = 16384
#str1 = 'handshake'
#str2 = 'shake hands'
#answer = 65536
#str1 = 'aa1+aa2'
#str2 = 'AAAA12'
#answer = 43690
str1 = 'E=M*C^2'
str2 = 'e=m*c^2'
print(news_clustering(str1, str2))