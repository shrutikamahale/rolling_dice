#Python Program - Implement Bubble Sort
def bubbleSort(arr):
	n = len(arr)
	for i in range(n):
		for j in range(0, n-i-1):

			if arr[j] > arr[j+1] :
				arr[j], arr[j+1] = arr[j+1], arr[j]
arr = [34,76,121,45,98,43,54,12]
bubbleSort(arr)
print ("Sorted array is:")
for i in range(len(arr)):
	print ("%d" %arr[i]), 
