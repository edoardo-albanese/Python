try:
    num = int(input("Insert number, will check if it's either even or odd: "))
    if (num & 2) == 0:
        print("Number is even")
    else:
        print("Number is odd")
except:
    print("Only insert numbers!")
