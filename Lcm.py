a=int(input())
b=int(input())
if a>b:
    c=a
else:
    c=b
for i in range(0, (a*b)+1):
      if c%a==0 and c%b==0:
         print(c)
         break   
      c=c+1   
