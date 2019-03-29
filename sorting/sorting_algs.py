#sorting algorithm
import time


def bubbleSort(alist):
	start = time.time()
	for loop_count in range(len(alist)-1, 0, -1):
		for idx in range(loop_count):
			if alist[idx] > alist[idx+1]:
				tmp = alist[idx]
				alist[idx] = alist[idx+1]
				alist[idx+1] = tmp
	curr_time = time.time() - start
	return alist, curr_time

def selectionSort(alist):
	start = time.time()
	for offset in range(0, len(alist)-1):
		offset_minValue = offset
		for num in range(offset+1, len(alist)):
			if alist[num] < alist[offset_minValue]:
				offset_minValue = num
		tmp = alist[offset_minValue]
		alist[offset_minValue] = alist[offset]
		alist[offset] = tmp
	curr_time = time.time() - start
	return alist, curr_time

def insertinoSort(alist):
	start = time.time()
	for index in range(1, len(alist)):
		currentvalue = alist[index]
		position = index

		while position > 0 and alist[position-1] > currentvalue:
			alist[position]=alist[position-1]
			position = position - 1
	alist[position] = currentvalue
	curr_time = time.time() - start
	return alist, curr_time

