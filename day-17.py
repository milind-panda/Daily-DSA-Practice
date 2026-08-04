def linear_search(arr, target):
  for i in range(0,len(arr)):
    if arr[i]==target:
      return i
  return -1

arr=[2,4,3,1,3,4,52,5,4]
target=4

print(linear_search(arr, target))
