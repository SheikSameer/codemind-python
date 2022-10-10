n=int(input())
sqr=n**2
sum=0
while sqr>0:
    digit=sqr%10
    sum=sum+digit
    sqr=sqr//10
if sum==n:
    print("Neon Number")
else:
    print("Not Neon Number")