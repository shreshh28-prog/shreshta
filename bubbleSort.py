lst = []
size = int(input('enter the size of array'))
for i in range(size):
  ele = int(input('enter elements of array'))
  lst.append(ele)

def bubbleSort(lst1):
  for j in range(0,size-1):
    temp = true
    for k in range(0,size-j-1):
      if lst1[k]>lst1[k+1]:
        lst1[k],lst1[k+1] = lst1[k+1],lst1[k]
        temp = false
  if temp:
    break
return lst1

print('sorted list is :',bubbleSort(lst))
        
  
