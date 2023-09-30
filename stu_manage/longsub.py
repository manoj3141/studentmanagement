while True:
 string=input('enter the str:')
 sub=''
 list=[]
 for i in string:
    if i  not in sub: 
        sub=sub+i
        #print(sub)
    else:
        temp=sub
        sub=''
        k=temp.index(i)
        for j in range(k+1,len(temp)):
                sub=sub+temp[j]
        sub=sub+i        
    list.append(sub)  
 print(list) 
 m=0   
 for i in list:
    if len(i)>m:
        m=len(i) 
        sub=i
 print(sub)                       