#secret map

#input type :
#n (line number)
#arr1
#arr2

#output= bitwise or operation
'''
n = 5
arr1 = [9,20,28,18,11]
arr2 = [30,1,21,17,28]
'''
n = 6
arr1 = [46,33,33,22,31,50]
arr2 = [27,56,19,14,14,10]
def secret_map(arr1,arr2,n):
	ret_list = []
	for i in range(n):
		zeros = '0'*n
		a1 = bin(arr1[i])[2:]
		a1 = zeros[:n-len(a1)] + a1
		a2 = bin(arr2[i])[2:]
		a2 = zeros[:n-len(a2)] + a2

		#print(a2)
		#compare a1 and a2 and finally append ###s to ret_list
		ret_str = ''
		for i in range(n):
			if a1[i]=='1' or a2[i]=='1':
				ret_str += '#'
			else:
				ret_str += ' '
		ret_list.append(ret_str)
	return ret_list

print(secret_map(arr1, arr2, n))