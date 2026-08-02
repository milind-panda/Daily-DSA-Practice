#second largest element of an array
arr=[1,3,4,2,5,7,3,5,56]
largest=arr[0]
second_largest=arr[0]
for i in range(0,len(arr)):
  if arr[i]>largest:
    second_largest=largest
    largest=arr[i]
  elif arr[i]>second_largest and arr[i]>=largest:
    second_largest=arr[i]
print(second_largest)






#largest element in arrray
#1 sort it and print the last element
#2takr the 1st elememt as largest and compare
arr=[1,3,4,2,56]
largest=arr[0]
for i in range(0,len(arr)):
  if arr[i]>largest:
    largest=arr[i]
print(largest)  

#tc=O(n) 
