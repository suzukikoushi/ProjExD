import random
moji=10
kesson=2
def wards():
    w=[]
    t=[]
    for i in range(26):
        w += chr(i+65)
    n=25
    for j in range(moji):
        x=w[random.randint(0,n)]
        t+=x
        del x
        n-1
    return(t)
def b(t):
    k=[]
    for i in range(kaisuu):
         k+=t[random.randint(0,len(t))]
    return(k)
