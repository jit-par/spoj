# your code goes here
#input the values and just find the place where 'machula' is placed
#and you have ur answer
for i in range(int(input())):
    t=input()
    t1 ,op1 ,t2 ,op2 ,res=input().split()
    if('machula' in t1):
        print(int(res)-int(t2),op1,t2,op2,res)
    elif('machula' in t2):
        print(t1,op1,int(res)-int(t1),op2,res)
    elif('machula' in res):
        print(t1,op1,t2,op2,int(t1)+int(t2))
