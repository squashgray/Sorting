# TO-DO: Complete the selection_sort() function below 

def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        for j in range(i+1, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j

        arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index] 




    return arr

arr2 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    go = True
    while go:
        for i in range(0, len(arr) - 1):
            cur_index = i
            j = i+1
            print(cur_index)
            if arr[j] < arr[cur_index]:
                arr[cur_index], arr[j] = arr[j], arr[cur_index]
                go = True
            else:
                go = False
           
                

            
    


        
    return arr
print(bubble_sort(arr2))

# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr