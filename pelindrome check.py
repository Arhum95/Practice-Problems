num=int(input())
a=num
b=num
num2=0
j=1
i=0
while(a>0):
        a=int(a/10)
        i=i+1
while(b>0):
       c=b%10
       b=int(b/10)
       num2=num2+(c*(10**(i-j)))
       j=j+1      
if num2 == num:
        print("Your number is pelindrome")
else:
    print ("Your number is not pelindrome")        
