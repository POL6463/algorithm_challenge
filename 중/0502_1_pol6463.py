inputNum = int(input())
num = 1
degree = 1


while(num < inputNum):
    num += 6 * degree
    degree += 1

print(degree)