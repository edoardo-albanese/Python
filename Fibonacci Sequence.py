print("This is the fibonacci sequence")

numbers = []
max_n = int(input("How many numbers shall there be?"))
a = 0
b = 1
numbers.append(a)
numbers.append(b)

index = 0
while index <= max_n - 3:
    c = a + b
    a = b
    b = c
    numbers.append(c)
    index += 1
print(numbers)