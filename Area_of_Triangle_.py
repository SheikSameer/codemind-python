a,b,c=map(int,input().split())
s=(a+b+c)/2
area=(s*(s-a)*(s-b)*(s-c))**0.5
print("{:.2f}".format(area))