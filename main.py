num = 269
# 2 + 6 + 9 == 17 => 1 + 7 == 8
#  865 => 8 + 6 + 5 == 19 => 1 + 9 == 10 => 1 + 0 == 1


def sum_number_char(number):
    str_number = str(number)
    sum_number = 0
    for i in range(len(str_number)):
        sum_number += int(str_number[i])
    return sum_number


list_all = []
number = input("Plz enter a number : ")

for i in range(int(number)):
    a = 0
    a = sum_number_char(i)
    if a > 9:
        a = sum_number_char(a)
        if a > 9:
            a = sum_number_char(a)
    # print(a)
    list_all.append(a)
    # if a == 1:
    #     list_one.append(a)
    # elif a == 2:
    #     list_two.append(a)

number_of_one = 0
number_of_two = 0
for i in list_all:
    if i == 1:
        number_of_one += 1
    elif i == 2:
        number_of_two += 1

print("Number of One: ", number_of_one)
print("Number of Two: ", number_of_two)
