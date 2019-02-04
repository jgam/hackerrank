#cache

#LRU, we need to use Queue and Hash.
#Queue is implemented using a doubly linked list. The maximum size of the queue will be equal toi the toal number of frames

#Hash with page number as key and address of the corresponding queue node as value.

#cache hit = 1
#cache miss = 5

#input
#cache size, cities

def get_cache(size, array):
	#input is the array
	ret_num = 0
	array = [i.upper() for i in array]
	for index in range(size, len(array)):
		#do some
		if array[index] in array[index-size:index]:
			ret_num += 1
		else:
			ret_num += 5
	return ret_num + (5*size)

array = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]
cache_size = 3

print(get_cache(cache_size, array))

array = ["Jeju", "Pangyo", "NewYork", "newyork"]
cache_size = 2
print(get_cache(cache_size, array))

array=["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]
cache_size = 0
print(get_cache(cache_size, array))

array=["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]
cache_size = 5
print(get_cache(cache_size, array))