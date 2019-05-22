choice=int(input("Enter Choice 1 for binary or 2 for Octal: "))
if choice == 1:
   num=int(input("Enter a Decimal number: "))
   print("Binary equivalent is:",end='')
   a=num
   rem = []
   while(num>0):
       rem.append(num%2)
       num=int(num/2)
   while(a>0):
       a=int(a/2)
       s=rem.pop()
       print(s,end='')

elif choice == 2:   
     num=int(input("Enter a Decimal number: "))
     print("Octal equivalent is:",end='')
     a=num
     rem = []
     while(num>0):
        rem.append(num%8)
        num=int(num/8)
     while(a>0):
        a=int(a/8)
        s=rem.pop()
        print(s,end='')
else:
    print("invalid choice")   
   
