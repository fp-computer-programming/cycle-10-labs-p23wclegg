#Lab_10-1

sum = 0
#Making a base number for addition
while True: 
    num = (input('number: '))
    if num == -1:
        #While loop that allows for inputs of nubmers other than -1
        print(sum) 
    sum += num
    break 
#Required break to exit the loop