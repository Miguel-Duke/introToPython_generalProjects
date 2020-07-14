
userDigits = int(input())

jobDone = False

if userDigits < 20:
    print('Input must be 20-98')
elif userDigits > 98:
    print('Input must be 20-98')
else:
    stringDigits = str(userDigits)
    digitOne = stringDigits[0]
    digitTwo = stringDigits[1]
    
    while jobDone != True:
        
        if digitOne != digitTwo:
            print(digitOne + digitTwo)
            userDigits -= 1
            stringDigits = str(userDigits)
            digitOne = stringDigits[0]
            digitTwo = stringDigits[1]
            
        else:
            print(digitOne + digitTwo)
            jobDone = True
