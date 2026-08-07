#optimal: kadane
n=len(arr)
maxi=float("-inf")
total=0
for i in range(0,n):
  total=total+arr[i]
  maxi=max(maxi,total)
  if total<0:
    total=0
print(maxi)
