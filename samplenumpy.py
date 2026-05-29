import numpy as np

array1 = np.zeros(3)
array2 = np.zeros((1,4))
array3= np.zeros((2,5))

print(array1)
print(array2)
print(array3)
print(array1[0] , array1[2])
print(array2[0][0] , array2[0][3])
print(array3[1][0] , array3[1][3])

try:
 print(array1[4])

except IndexError :
  print("You have tried to access a fourth element but there are only 3 elements.")

except:
 print("Some error has occured.Sorry for the inconvinience")
