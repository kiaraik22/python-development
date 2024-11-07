
age = 22
if age < 20:
    print('Error')
    if age < 15:
        print('Fatal')
elif age < 25:
    print('25 Ok')
else:
    print('Ok')
print('Next')

# цикл for

# numbers = [1,2,3,4,5,6,7,8,9,10]
# N = 11
#
# for i in range():
#     print(i)


# cars = ['ford', 'audi', 'lada']
# N = 10
#
# for ind_car in range(len(cars)):
#     print(ind_car, cars[ind_car])

a = 10
b = 0

while a < 20:
    print(a)

    b+=1

    if b == 15:
        break