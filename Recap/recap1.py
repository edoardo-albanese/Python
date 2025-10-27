def operate_numbers(num1, num2):
    print("The number sum is ", str(num1 + num2))
    print("The number minus the other is ", str(num1 - num2))
    print("The number times the other is ", str(num1 * num2))
    try:
        print("The number divided by the other is ", str(num1 / num2))
    except:
        print("Error: division by 0")

try:
    number1 = float(input("Insert the first number: "))
    number2 = float(input("Insert the second number: "))
    operate_numbers(number1, number2)
except:
    print("Use numbers!")

