num1=0
while num1 < 3:
    print("Which Operation do you want to perform:")
    print("\nType 1 for Insertion Sort")
    print("\nType 2 for Quick Sort")
    print("\nType 3 for Selection Sort")
    print("\nType 4 for ***Exit***")
    uchoice=input("\nWhich Operation do you want to perform:")


    match uchoice:

        case '1':
            def insertionSort(arr):
  
                for i in range(1, len(arr)):
                    key = arr[i]
  
                    j = i-1
                    while j >=0 and key < arr[j] :
                        arr[j+1] = arr[j]
                        j -= 1
                    arr[j+1] = key
  
            arr = [12, 11, 13, 5, 6]
            print("Unsorted array:",arr)
            insertionSort(arr)
            print ("Sorted array is:")
            for i in range(len(arr)):
                print ("%d" %arr[i])

        case '2':
            def partition(array, low, high):

                pivot = array[high]


                i = low - 1

  
                for j in range(low, high):
                    if array[j] <= pivot:
    
                        i = i + 1
                        (array[i], array[j]) = (array[j], array[i])

 
                (array[i + 1], array[high]) = (array[high], array[i + 1])

 
                return i + 1


            def quickSort(array, low, high):
                if low < high:

                    pi = partition(array, low, high)
                    quickSort(array, low, pi - 1)
                    quickSort(array, pi + 1, high)


            data = [8, 7, 2, 1, 0, 9, 6]
            print("Unsorted Array",data)
            print(data)
            size = len(data)
            quickSort(data, 0, size - 1)
            print('Sorted Array in Ascending Order:')
            print(data)

        case '3':
            
            import sys
            A = [64, 25, 12, 22, 11]
            
            print("Unsorted Array")
            for i in range(len(A)):
                print("%d" %A[i]), 

            for i in range(len(A)):
                    
                min_idx = i
                for j in range(i+1, len(A)):
                    if A[min_idx] > A[j]:
                        min_idx = j
                                
                A[i], A[min_idx] = A[min_idx], A[i]
            

            print ("Sorted array")
            for i in range(len(A)):
                print("%d" %A[i])

    num1 = uchoice
    num1=int(num1)
            

