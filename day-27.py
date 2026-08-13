#rearrange elements by sign
arr=[5,10,-3,-1,-10,6]
#result=[5,-3,10,-1,6,-10] alternative way
lis1=[]
lis2=[]
for i in arr:
  if i<0:
    lis1.append(i)
  else:
    lis2.append(i) 
for i in range(0,len(lis1)):
  arr[2*i]=lis1[i]
  arr[2*i+1]=lis2[i]
print(arr)     
