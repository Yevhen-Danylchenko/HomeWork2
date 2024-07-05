numbers = [3,1,2,4,5]

num1 = []
num2 = []

for index in range(len(numbers)) :

    if numbers[index] % 2 == 0 :
        num1.append(numbers[index])
    else:
        num2.append(numbers[index])

numbers = num1.copy() + num2.copy()

print(numbers)
