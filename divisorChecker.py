###Taking inputs from user
print('Enter a number:')
number = int(input())
for i in range(1,number):
    if(number % i==0):
        print(i)
