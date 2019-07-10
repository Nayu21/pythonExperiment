list = []
userInput = int(input())
for i in range(userInput):
    temp = int(input())
    list.append(temp)
maximum = 0
for j in range(len(list)):
    if list[j]>maximum:
        maximum = list[j]
print(maximum)
