number = int(input("Type any number :"))
if number > 0: 
    for i in range(1, 11):
        mull=number*i
        print(number," x",i,"=",mull,end="")
        print('')    
else:  print(number,"is Invalid number")
