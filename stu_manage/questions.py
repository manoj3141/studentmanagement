#1.factoprial
'''n=int(input('enter to factnorial:'))
for i in range(n-1,1,-1):
    n=n*i
print(n)    '''

#2.armstrong:
'''a=str(input('enter to armstrong:'))
b=len(a)
ans=0
for i in a:
    ans=pow(int(i),b)+ans
if ans==int(a):
    print('armstrong')
else:
    print('not armstrong')'''
    
#3:prime or not:
'''p=int(input('enter to prime or not:'))
for i in range(p-1,1,-1):
    if p%i==0:
        print('not prime')
        break
    elif i==2:
        print('prime')'''
        
#4.pattern:
'''n=int(input('enter to pattern:'))
for i in range(1,n+1):
    
    for j in range(i):
        print('*',end='')
        
    print('\n')        
    
n=int(input('enter to pattern:'))
for i in range(n+1,1):
    
    for j in range(i):
        print('*',end='')
        
    print('\n')  '''
    
#5.reverse triangle

'''n=int(input('enter to pattern:'))
for i in range(1,n+1):
    for j in range(i,n):
        print(" ",end='')
    for k in range(i):
         print('*',end='')
    print('\n') '''    
            
#6.            
'''n=str(input('enter to add:'))
sum=0
for i in n:
    sum=int(i)+sum
print(sum)    '''

#7.Finding second heightest number in a list
n = int(input("Enter the size of list"))
nums = []
for i in range(n):
    val = int(input("Enter a value"))
    nums.append(val)
nums
big = max(nums[0],nums[1])
sec_mx = min(nums[0],nums[1])
for i in range(2,n):
    if nums[i]>big:
        sec_mx = big
        big = nums[i]
    elif nums[i]>sec_mx and big != nums[i]:
        sec_mx = nums[i]
    elif big == sec_mx and sec_mx != nums[i]:
        sec_mx = nums[i]

print("The second highest number in the list is:", sec_mx)
        
