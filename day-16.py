#right rotate by k place
#arr=[3,9,5,6,7,2] ,k=3
#[6,7,2,3,9,5]
arr=[3,9,5,6,7,2]
k=3
n=len(arr)
arr=arr[n-k:n]+arr[0:n-k]
print(arr)




#right rotate an array by 1 place
#arr=[1,2,3,4,5]
#[5,1,2,3,4]
arr=[1,2,3,4,5,6]
n=len(arr)
arr=[arr[-1]]+arr[0:n-1]
print(arr)



def check_if_sorted(arr):
  for i in range(0,len(arr)-1):
    if arr[i]>arr[i+1]:
      return False # If an element is greater than the next, it's not sorted
  return True # If the loop completes, the array is sorted

arr=[1,2,3,4,5]
print(check_if_sorted(arr))

arr2=[1,3,2,4,5]
print(check_if_sorted(arr2))
