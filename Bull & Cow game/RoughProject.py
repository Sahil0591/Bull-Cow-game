import random
cond = False
#cond helps to get a random integer above 999
while cond == False:
    x = 0
    ra = random.randint(1000,9999)
    #integer digits as elements of list
    a = list(map(int, str(ra)))
    for i in range(0, 4):
        cnt = a.count(a[i])
        x = x + cnt
    if (x == 4):
        cond = True
print(ra)
print()



#cond2 checks if the user has found the correct sequence
cond2 = False
count = 0
cow = 0
bull = 0
while cond2 == False:
    tc = 0
    tb = 0
    count += 1
    #cond3 is to obtain a unique 4 digit number from the user
    cond3 = False
    while cond3 == False:
        x = 0
        num = int(input("Enter Number : "))
        a1 = list(map(int, str(num)))

        for i in range(0,4):
            try:
                cnt = a1.count(a1[i])
            #For when the user enters a number less than 1000 and greater than 9999
            except IndexError:
                print("Please enter a unique four digit number greater than 999 and less than 10000")
                print("Where the digits are non-repeating")
                print()
                break
            x = x + cnt
        if(x == 4):
            cond3 = True
        #If a user inputs a number with repeating digits
        else:
            print("Please enter a unique number, where the digits are non-repeating")
            print()
    #cross-checking the digits of the entered number and the unique number
    for i in range(0,4):
        for j in range(0,4):
            #cow
            if (a[i] == a1[i]):
                tc = tc+1
                break
            #bull
            elif(a[i] == a1[j]):
                tb = tb+1
                break
    print("Cow = ",tc)
    print("bull =",tb)
    print()
    cow = tc
    if(cow == 4):
        cond2 = True
print("You have found the hidden number! :",num)
print("It took you",count,"tries to crack the code")