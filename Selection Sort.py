
unsortedFile =  open('numbers.txt', 'r')
sortedFile = open('sorted.txt', 'w')
arr = unsortedFile.read().split('\n')       #in its current state, the numbers are strings not integers
arr = list(map(int, arr))       #this converts number strings into integers
unsortedFile.close()
sortedArr = []

def selectionSort(array, sort):
    for minimum in range(len(array)):
        for current in range(minimum, len(array)):
            if sort == 'asc':
                if array[current] < array[minimum]:
                    temp = arr[minimum]
                    array[minimum] = array[current]
                    array[current] = temp
            elif sort == 'desc':
                if array[current] > array[minimum]:
                    temp = array[current]
                    array[current] = array[minimum]
                    array[minimum] = temp
    return array

while True:
    sort = str(input("Sort ascending or descending? ('asc' or 'desc') "))
    if sort == 'asc':
        break
    elif sort == 'desc':
        break

#print("Original: " + str(arr))
#print("Sorted (Ascending): " + str(selectionSort(arr, 'asc')))
#print("Sorted (Descending): " + str(selectionSort(arr, 'desc')))
sortedArr = selectionSort(arr, sort)
for number in sortedArr:
    sortedFile.write(str(number) + "\n")
sortedFile.close()
print("Successfully sorted the numbers in " + sort + " order, exported to 'sorted.txt'")
