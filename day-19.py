arr = [5, 9, 1, 2, 4, 15, 6, 3]
target = 13

seen = {}

for i in range(len(arr)):
    complement = target - arr[i]

    if complement in seen:
        print(seen[complement], i)
        break

    seen[arr[i]] = i



#max consecutive ones
arr=[1,1,0,1,1,1]
count=0
i=0
while(i<len(arr)):
  if arr[i]==1:
    count+=1
  else:
    count=0
  i+=1
print(count)





#find the missing value
nums=[0,1,3,4]
nums.sort()
for i in range(0,len(nums)):
  if nums[i]!=i:
    print(i)
    break
