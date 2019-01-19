#Taking numbers from user
print('Enter a number:')
number = int(input())
temp = 0
for i in range(1,number):
    if(number % i == 0 ):
        temp += i
    
if(temp==number):
    print(''+str(number)+' is perfect number')
else:
    print(''+str(number)+' is not perfect number')
