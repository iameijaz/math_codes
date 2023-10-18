# Author: VBT 
# Date: 10/18/2023 
# Collatz_Conjecture.py
# 10/18/2023   --> 3x+1 Conjecture
# https://www.youtube.com/watch?v=094y1Z2wpJg&pp=ygUSY29sbGF0eiBjb25qZWN0dXJl --> The Simplest Math Problem No One Can Solve - Collatz Conjecture (Veritasium) 
# https://www.youtube.com/watch?v=5mFpVDpKX70&pp=ygUSY29sbGF0eiBjb25qZWN0dXJl --> UNCRACKABLE? The Collatz Conjecture - Numberphile




def collatz(n, cont=0, printing=True):
    '''
    leave printing True if you want to see the series
    it returns the number of steps while priting the steps
    you can modify it to get it in the form of a list, but it can become computationally expensive for larger steps
    '''
    if(n==1):
        if(printing):
            print(1)
        cont=cont+1
        return cont
    elif(n%2==0):
        if(printing):
            print(n,end=",")
        return collatz(int(n/2), cont+1,printing=printing)
    else:
        if(printing):
            print(n, end=",")
        return collatz(3*n+1, cont+1,printing=printing)
cnt=0


#for i in range(1,1000000):
#    cnt=collatz(i, printing=False)
#    if(cnt>100):
#        print(i," -- >  ", str(cnt))
#        print("-"*20)
        #break # if you only need one with that steps

n=collatz(27)
print(f"Total N steps : {n}")

