
def selection_sort(arr):
	#fiding the minimum number and place it in indexes of increasing orders.
	for i in range(len(arr)):
		min_num = a[i]
		position = i
		for j in range(i+1,len(arr)):
			if min_num > a[j]:
				min_num = a[j]
				position = j
		arr[position] = arr[i]
		arr[i] = min_num
	return arr
#time complexity = O(n^2)
#auxiliary Space = O(1)


def bubble_srot(arr):
	#swap the indexes of elements in the array
	