#implementation of merge sort algorithm

#function for the merge sort 
def merge_sort(arr):
    if len(arr) > 1:
        #splilting the array into two part-----
        mid = len(arr)//2
        #Dividing the element in the array 
        Right = arr[mid:]
        Left  = arr[:mid]

        merge_sort(Right)
        merge_sort(Left)

        i = j = k = 0
        while i < len(Left) and j < len(Right):
            if Left[i] <= Right[j]:
                arr[k] = Left[i]
                i +=1
            else:
                arr[k] =Right[j]
                j +=1
            k +=1
        #check if there is some element left 
        while i < len(Left):
            arr[k] = Left[i]
            i +=1
            k +=1
        
        while j < len(Right):
            arr[k] = Right[j]
            j +=1
            k +=1

if __name__ == "__main__":
    print("Enter the array")
    arr = list(map(int, input().split()))
    merge_sort(arr)
    print("sorted array")
    for i in range(len(arr)):
        print("%d" % arr[i], end=" ")

        
