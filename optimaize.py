number = int(input('Enter a number: '))
num = int(number / 9)
number_of_one = num
number_of_two = num
if int(number) % 9 == 1:
    number_of_one += 1
elif int(number) % 9 == 2:
    number_of_one += 1
    number_of_two += 1
else:
    number_of_one += 1
    number_of_two += 1

print("Number of one is ", number_of_one)
print("Number of two is ", number_of_two)

# [1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,1]
