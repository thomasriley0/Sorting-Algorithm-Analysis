def selectionSort(L):
    i = 0
    # invariant: L[0:i] sorted and in final position
    while i < len(L):
        minIndex = findMinIndex(L, i)
        L[i], L[minIndex] = L[minIndex], L[i]
        # now L[0:i+1] sorted an in final position.
        i = i + 1
        # L[0:i] sorted/in final position,and "loop invariant" (loop entry point assumption) holds again

        ## uncomment this if you want to see progress (don't do for large L though!)
        #print("sorted and in final pos:", L[0:i], "unsorted:", L[i:])

# return index of min item in L[startIndex:]
# assumes startIndex < len(L)
#
def findMinIndex(L, startIndex):
    minIndex = startIndex
    currIndex = minIndex + 1
    while currIndex < len(L):
        if L[currIndex] < L[minIndex]:
            minIndex = currIndex
        currIndex = currIndex + 1
    return minIndex

def insertionSort(L):
    i = 1
    
    # invariant: L[0:i] is sorted
    while i < len(L):
        itemToMove = L[i]
        # find where itemToMove should go, shifting larger items right one slot along the way
        j = i-1
        while ((j>=0) and (itemToMove<L[j])):
            L[j+1] = L[j]
            j = j-1

        # found the spot - put itemToMove there
        L[j+1] = itemToMove

        # now L[0:i+1] is sorted (though items not necessarily in final position)
        i = i + 1
        # L[0:i] sorted and "loop invariant" (loop entry point assumption) holds again

        ## uncomment this if you want to see progress (don't do for large L though!)
        #print("sorted:", L[0:i], "unsorted:", L[i:])
        
    return

# Recursive version of merge sort.  
# (It's much easier for most people to correctly implement mergesort recursively.)
# Note: this version modifies L itself, like the other sorts.
#
def mergeSort(L):
    if (len(L) < 2):
        return 
    else:
        # 1. divide list into (almost) equal halves
        middleIndex = len(L)//2
        left = L[:middleIndex]
        right = L[middleIndex:]
        
        #2. recursively sort left and right parts
        mergeSort(left)
        mergeSort(right)
        
        #3. merge sorted left/right parts
        mergedL = merge(left, right)
        
        # mergedL is now sorted but we need to do one more thing (related to Note above)
        # this copies the contents of margedL into L
        L[:] = mergedL[:]
        return
    
# Merge function used by both the recursive and non-recursive merge sorts.
def merge(L1, L2):
    mergedL = []
    iL1 = 0
    iL2 = 0

    while iL1 != len(L1) and iL2 != len(L2):
        if L1[iL1] <= L2[iL2]:
            mergedL.append(L1[iL1])
            iL1 = iL1 + 1
        else:
            mergedL.append(L2[iL2])
            iL2 = iL2 + 1

    # At this point, we've used up all the items from one of the lists.
    # Use list "extend" method to add all the remaining items to mergedL
    mergedL.extend(L1[iL1:])
    mergedL.extend(L2[iL2:])

    return mergedL

def builtinSort(L):
    L.sort()
    
# Python3 program for implementation
# of Iterative Heap Sort

# function build Max Heap where value
# of each child is always smaller
# than value of their parent
def buildMaxHeap(arr, n):

	for i in range(n):
		
		# if child is bigger than parent
		if arr[i] > arr[int((i - 1) / 2)]:
			j = i
	
			# swap child and parent until
			# parent is smaller
			while arr[j] > arr[int((j - 1) / 2)]:
				(arr[j],
				arr[int((j - 1) / 2)]) = (arr[int((j - 1) / 2)],
										arr[j])
				j = int((j - 1) / 2)

def heapSort(arr, n):

	buildMaxHeap(arr, n)

	for i in range(n - 1, 0, -1):
		
		# swap value of first indexed
		# with last indexed
		arr[0], arr[i] = arr[i], arr[0]
	
		# maintaining heap property
		# after each swapping
		j, index = 0, 0
		
		while True:
			index = 2 * j + 1
			
			# if left child is smaller than
			# right child point index variable
			# to right child
			if (index < (i - 1) and
				arr[index] < arr[index + 1]):
				index += 1
		
			# if parent is smaller than child
			# then swapping parent with child
			# having higher value
			if index < i and arr[j] < arr[index]:
				arr[j], arr[index] = arr[index], arr[j]
		
			j = index
			if index >= i:
				break
            
def median(a, b, c):
    if ( a - b) * (c - a) >= 0:
        return a

    elif (b - a) * (c - b) >= 0:
        return b

    else:
        return c
            
def quicksort(array):
    leftend = 0
    rightend = len(array)
    
    ## We define our 3 arrays
    less = []
    equal = []
    greater = []

    ## if the length of our array is greater than 1
    ## we perform a sort
    if len(array) > 1:
        ## Select our pivot. This doesn't have to be
        ## the first element of our array
         left = array[leftend]
         right = array[rightend-1]
         length = rightend - leftend
         if length % 2 == 0:
             middle = array[int(leftend + length/2 - 1)]
         else:
             middle = array[int(leftend + length/2)]
  
    

         pivot = median(left, right, middle)
         pivotindex = array.index(pivot)
         array[pivotindex] = array[leftend]
         array[leftend] = pivot


        ## recursively go through every element
        ## of the array passed in and sort appropriately
         for x in array:
            if x < pivot:
                less.append(x)
            if x == pivot:
                equal.append(x)
            if x > pivot:
                greater.append(x)

        ## recursively call quicksort on gradually smaller and smaller
        ## arrays until we have a sorted list.
         return quicksort(less)+equal+quicksort(greater)

    else:
        return array
            

import random
# return a new list with the same elements as input L but randomly rearranged
def mixup(L):
    newL = L[:]
    length = len(L)
    for i in range(length):
        newIndex = random.randint(i,length-1)
        newL[newIndex], newL[i] = newL[i], newL[newIndex]
    return(newL)

##########

import time

def timeSort(sortfn, L):
    t1 = time.time()
    sortfn(L)
    t2 = time.time()
    return (t2 - t1)

# try, e.g.,
# l = mixup(list(range(4000)))
# timeAllSorts(l)
def timeAllSorts(L):

    Lcopy = L[:]
    sTime = timeSort(selectionSort, Lcopy)
    Lcopy = L[:]
    iTime = timeSort(insertionSort, Lcopy)
    Lcopy = L[:]
    mTime = timeSort(mergeSort, Lcopy)
    Lcopy = L[:]
    biTime = timeSort(builtinSort, Lcopy)
    
    print("{}\t sel: {:.2f}\t ins: {:.2f}\t merge: {:.2f}\t builtin: {:.2f}".format(len(L), sTime, iTime, mTime, biTime))


# The code below is commented out (with ''' before and after) so that the code above will run even
# when you are using a Python that does not have pylab.  If you are using a Python
# with pylab, remove the '''s.
# As demonstrated in Lectures 30 and 31, you can call "compareSorts" to produce a chart graphing
# running times of selection and insertion sort on randomly ordered lists of various sizes.
# For HW 7, use several functions like this (with additional sorting methods) to compare all the
#sorting methods on various kinds of data
#
import pylab
def compareSorts(slowMinN = 250, slowMaxN=2000, fastMinN = 10000, fastMaxN = 250000, step=250, fastStep=25000):
    
    mergeSortTimes = []
    builtInSortTimes = []
    selectionSortTimes = []
    insertionSortTimes = []
    heapSortTimes = []
    quickSortTimes = []
    
    reverseMergeSortTimes = []
    reverseBuiltInSortTimes = []
    reverseSelectionSortTimes = []
    reverseInsertionSortTimes = []
    reverseHeapSortTimes = []
    reverseQuickSortTimes = []
    
    sortedMergeSortTimes = []
    sortedBuiltInSortTimes = []
    sortedSelectionSortTimes = []
    sortedInsertionSortTimes = []
    sortedHeapSortTimes = []
    sortedQuickSortTimes = []
    
    
    slowListSizes = list(range(slowMinN, slowMaxN, step))
    fastListSizes = list(range(fastMinN, fastMaxN, fastStep))


    for listSize in slowListSizes:
        #slow sorts random lists
        listToSortOrig = mixup(list(range(0, listSize)))
        listToSort = listToSortOrig[:]
        startTime = time.time()
        selectionSort(listToSort)
        endTime = time.time()
        selectionSortTimes.append(endTime-startTime)
        listToSort = listToSortOrig[:]
        startTime = time.time()
        insertionSort(listToSort)
        endTime = time.time()
        insertionSortTimes.append(endTime-startTime)
    #slow sorts already sorted
        listToSortOrig = (list(range(0, listSize)))
        listToSort = listToSortOrig[:]
        startTime = time.time()
        selectionSort(listToSort)
        endTime = time.time()
        sortedSelectionSortTimes.append(endTime-startTime)
        listToSort = listToSortOrig[:]
        startTime = time.time()
        insertionSort(listToSort)
        endTime = time.time()
        sortedInsertionSortTimes.append(endTime-startTime)
    #slow sorts reverse sorted
        listToSortOrig = (list(range(0, listSize)))
        listToSort = listToSortOrig[::-1]
        startTime = time.time()
        selectionSort(listToSort)
        endTime = time.time()
        reverseSelectionSortTimes.append(endTime-startTime)
        listToSort = listToSortOrig[::-1]
        startTime = time.time()
        insertionSort(listToSort)
        endTime = time.time()
        reverseInsertionSortTimes.append(endTime-startTime) 
    for listSize in fastListSizes:
    #fast sorts random
        listToSortOrig = mixup(list(range(0, listSize)))
        listToSort = listToSortOrig[:]
        startTime = time.time()
        mergeSort(listToSort)
        endTime = time.time()
        mergeSortTimes.append(endTime - startTime)
        listToSort = listToSortOrig[:]
        startTime = time.time()
        builtinSort(listToSort)
        endTime = time.time()
        builtInSortTimes.append(endTime - startTime)
        listToSort = listToSortOrig[:]
        startTime = time.time()
        heapSort(listToSort, len(listToSort))
        endTime = time.time()
        heapSortTimes.append(endTime - startTime)
        listToSort = listToSortOrig[:]
        startTime = time.time()
        quicksort(listToSort)
        endTime = time.time()
        quickSortTimes.append(endTime - startTime)

   
    #fast sorts already sorted
        listToSortOrig = (list(range(0, listSize)))
        listToSort = listToSortOrig[:]
        startTime = time.time()
        mergeSort(listToSort)
        endTime = time.time()
        sortedMergeSortTimes.append(endTime - startTime)
        listToSort = listToSortOrig[:]
        startTime = time.time()
        builtinSort(listToSort)
        endTime = time.time()
        sortedBuiltInSortTimes.append(endTime - startTime)
        listToSort = listToSortOrig[:]
        startTime = time.time()
        heapSort(listToSort, len(listToSort))
        endTime = time.time()
        sortedHeapSortTimes.append(endTime - startTime)
        listToSort = listToSortOrig[:]
        startTime = time.time()
        quicksort(listToSort)
        endTime = time.time()
        sortedQuickSortTimes.append(endTime - startTime)


   #fast sorts reverse sorted
        listToSortOrig = (list(range(0, listSize)))
        listToSort = listToSortOrig[::-1]
        startTime = time.time()
        mergeSort(listToSort)
        endTime = time.time()
        reverseMergeSortTimes.append(endTime - startTime)
        listToSort = listToSortOrig[::-1]
        startTime = time.time()
        builtinSort(listToSort)
        endTime = time.time()
        reverseBuiltInSortTimes.append(endTime - startTime)
        listToSort = listToSortOrig[::-1]
        startTime = time.time()
        heapSort(listToSort, len(listToSort))
        endTime = time.time()
        reverseHeapSortTimes.append(endTime - startTime)
        listToSort = listToSortOrig[::-1]
        startTime = time.time()
        quicksort(listToSort)
        endTime = time.time()
        reverseQuickSortTimes.append(endTime - startTime)



    
    #slow random data
    pylab.figure(1)
    pylab.clf()
    pylab.xlabel('List size')
    pylab.ylabel('Time (s)')
    pylab.title("Time consumption of slow sorting algorithms on randomized data")
    pylab.plot(slowListSizes, selectionSortTimes, color='red', label="Selection", alpha=0.7)
    pylab.plot(slowListSizes, insertionSortTimes, color='green', alpha=0.7, label="Insertion")
    pylab.legend(loc='upper left', frameon=False)
    
   
    #slow sorted data
    pylab.figure(2)
    pylab.clf()
    pylab.xlabel('List size')
    pylab.ylabel('Time (s)')
    pylab.title("Time consumption of slow sorting algorithms on already sorted data")
    pylab.plot(slowListSizes, sortedSelectionSortTimes, color='red', label="Selection", alpha=0.7)
    pylab.plot(slowListSizes, sortedInsertionSortTimes, color="green", label="Insertion", alpha=0.7)
    pylab.legend(loc='upper left', frameon=False)
    
    # slow reverse sorted data
    pylab.figure(3)
    pylab.clf()
    pylab.xlabel('List size')
    pylab.ylabel('Time (s)')
    pylab.title("Time consumption of slow sorting algorithms on already reverse sorted data")
    pylab.plot(slowListSizes, reverseSelectionSortTimes, color='red', label="Selection", alpha=0.7)
    pylab.plot(slowListSizes, reverseInsertionSortTimes, color='green', label="Insertion", alpha=0.7)
    pylab.legend(loc='upper left', frameon=False)
    
    # fast random data
    pylab.figure(4)
    pylab.clf()
    pylab.xlabel('List size')
    pylab.ylabel('Time (s)')
    pylab.title("Time consumption of fast sorting algorithms on randomized data")
    pylab.plot(fastListSizes, heapSortTimes, color='blue', label="Heap", alpha=0.7)
    pylab.plot(fastListSizes, builtInSortTimes, color="green", label="Built-in", alpha=0.7)
    pylab.plot(fastListSizes, mergeSortTimes, color="red", label="Merge", alpha=0.7)
    pylab.plot(fastListSizes, quickSortTimes, color="orange", label="Quicksort", alpha=0.7)

    pylab.legend(loc='upper left', frameon=False)
    
    # fast sorted data
    pylab.figure(5)
    pylab.clf()
    pylab.xlabel('List size')
    pylab.ylabel('Time (s)')
    pylab.title("Time consumption of fast sorting algorithms on already sorted data")
    pylab.plot(fastListSizes, sortedHeapSortTimes, color='blue', label="Heap", alpha=0.7)
    pylab.plot(fastListSizes, sortedBuiltInSortTimes, color='green', label="Built-in", alpha=0.7)
    pylab.plot(fastListSizes, sortedMergeSortTimes, color="red", label="Merge", alpha=0.7)
    pylab.plot(fastListSizes, sortedQuickSortTimes, color="orange", label="Quicksort", alpha=0.7)
    
    pylab.legend(loc='upper left', frameon=False)
    
    #fast reverse sorted data 
    pylab.figure(6)
    pylab.clf()
    pylab.xlabel('List size')
    pylab.ylabel('Time (s)')
    pylab.title("Time consumption of fast sorting algorithms on already reverse sorted data")
    pylab.plot(fastListSizes, reverseHeapSortTimes, color='blue', label="Heap", alpha=0.7)
    pylab.plot(fastListSizes, reverseBuiltInSortTimes,  color='green', label="Built-in", alpha=0.7)
    pylab.plot(fastListSizes, reverseMergeSortTimes,  color="red", label="Merge", alpha=0.7)
    pylab.plot(fastListSizes, reverseQuickSortTimes, color="orange", label="Quicksort", alpha=0.7)

    pylab.legend(loc='upper left', frameon=False)
        



        


