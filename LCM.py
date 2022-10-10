a,b=map(int,input().split())
for i in range(1,b+1):
    m=a*i
    if m%b==0:
        print(m)
        break