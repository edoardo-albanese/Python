valid_divisors = []

number = int(input("What number do you choose?"))

if type(number) != int:
    print("You haven't chosen a number!")
elif number < 2:
    print("Number must be bigger than 1.")
else:
    for i in range(number):
        divisor = i + 1
        if number % divisor == 0:
            valid_divisors.append(divisor)
    if len(valid_divisors) == 2:
        print("Number is prime!")
    else:
        print("Number is not prime :(")
    print(valid_divisors)