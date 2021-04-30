def sum_number(num):
    sum = 0
    first_step = True

    while True:
        if first_step is True or int(sum) > 9:
            first_step = False
            if int(sum) > 9 and int(num) == 0:
                num = sum
                sum = 0
            while int(num) != 0:
                sum += int(num) % 10
                num = int(num) / 10
        else:
            break

    return sum


number_of_one = 0
number_of_two = 0
list_a = []
number = int(input("Enter a number: "))
for i in range(number):
    item = sum_number(i)
    list_a.append(item)
    if item == 1:
        number_of_one += 1
    elif item == 2:
        number_of_two += 1

print("Number of one is ", number_of_one)
print("Number of two is ", number_of_two)
print(list_a)
