def sum_of_digits(n):
    li=[]
    for i in str(n):
        li.append(int(i))
    return sum(li)

num = int(input('enter number: '))
while num > 10:
    num = sum_of_digits(num)

if num == 5:
    print('lucky number',num)
else:
    print('not a lucky number',num)    
 
    


    
    
        
    
