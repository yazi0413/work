from random import randint
num=randint(1,10)

flag =True

while(flag):
    guess=input("please input an int")
    if(guess>num):
        print "too big"
    elif(guess<num):
        print "too small"
    else:
        print "BINGO"
        flag=False
print " THE END "

