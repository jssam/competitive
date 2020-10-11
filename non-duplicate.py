def non_duplicate(arr):
	"""Function to find non-duplicate element.
		We will use XOR.
		Since, xor of two same integers is zero.
		After taking, xor of all elements in the array, 
		only non-duplicate element left out.
	"""
	n = len(arr) # size of the array
	ans = arr[0]

	for i in range(1, n):
		ans = ans^arr[i]
	return ans

arr = [3, 1, 0, 6, 6, 1, 0]
print(non_duplicate(arr))
