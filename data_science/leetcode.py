import sys

def maxSlideWindow(s,t,size):
    n=len(s)
    res=[]
    for i in range(0,n-size+1):
        num=0
        tmp=s[i:i+size]
        for j in t:
            if j in tmp:
                num +=1
        if num==size:
            res.append(tmp)
    return res
                
line=sys.stdin.readline().strip()
s,t=line.split()
n=len(s)
size=len(t)
for i in range(size,n):
    res=maxSlideWindow(s,t,i)
    if res:
        print(res)
        break
    