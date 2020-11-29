haveLength = False
upCase = False
lowCase = False
haveNum = False
counter = 0

Length = input("Does your password contain atleast 6 characters or more,'yes' or 'no' ?: ")
if Length.lower() == 'yes':
    haveLength = True
    counter +=1
Upper_case = input("Does your password have uppercase letters,'yes' or 'no' ?: ")
if Upper_case.lower() == 'yes':
    upCase = True
    counter +=1
Lower_case = input("Does your password have lowercase letters,'yes' or 'no' ?: ")
if Lower_case.lower() == 'yes':
    lowCase = True
    counter +=1
Numbers = input("Does your password contain numbers,'yes' or 'no' ?: ")
if Numbers.lower() =='yes':
    haveNum = True
    counter +=1


if counter >= 3:
    print('This is a suitable password ')

else:
    print('This is a not suitable password ')


