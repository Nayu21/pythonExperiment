list = []
userInput =int(input())
for i in range (userInput):
    temp = int(input())
    if (temp%2==0):
        list.append(temp)
print(list)
