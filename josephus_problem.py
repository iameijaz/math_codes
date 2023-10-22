from math import log2
''' 
Author: Verbit 
Date: 10/22/2023


https://www.youtube.com/watch?v=uCsD3ZGzMgE Numberphile Video


There are n people around a circle, and proceeding around the circle every second person is executed
until no one survives in n iterations. The Josephus Problem is to identify the initial position to be
the last survivor in this scenario.

'''


def safe_place(n):
    '''
    n : total number of people
    '''
    s=2*(n-pow(2,int(log2(n))))+1
    return s

n=41
print(f'Safe Place for {n} people would be:\n >> {safe_place(41)}')
