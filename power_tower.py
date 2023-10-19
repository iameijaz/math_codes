'''
Author: VBT
Date: 10//18/2023 

How Big is Graham's Number? (feat Ron Graham)
https://www.youtube.com/watch?v=GuigptwlVHo
Tower Notation using Python Recursive Functions
Knuth’s Up-arrow Notation 
https://hamzaalsamraee.com/blog/grahams-number
https://mathworld.wolfram.com/KnuthUp-ArrowNotation.html

'''

def get_exp(a,b):
    return a**b


def get_tower(a, b, c):
    '''
    a: the base digit
    b: number of arrows
    c: digit after arrow(s)
    get_tower(2,5,3) --> 2^^^^^3 --> 2^2^2^2^3
    '''
    if b==1:
        return (a**c)
    else:
        # 3**(3^4)
        return a**get_tower(a,b-1,c)

print("2^^^4 --> 2(3,4) ")
print(get_tower(2,2,4))
