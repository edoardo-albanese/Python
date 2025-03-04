import datetime

Months = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}

monthsId = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

#calcolo anno bisestile
year = datetime.datetime.today().year
if year % 4 == 0:
    Months[2] = 29

def create_input_var(prompt : str, error : str, type_ : type):
    while True:
        var = input(prompt)
    
        try:
            var = type_(var)
            break
        except ValueError:
            print(error)
    return var

def convert_from_year(date):
    if date < 1 or date > sum(Months.values()):
        print("Number is out of bounds!")
    else:
        i = 1
        month = 0
        day = date

        while day > Months[i]:
            day -= Months[i]
            month = i
            i += 1
        
        print(monthsId[month] + " the " + str(day))

def convert_from_month(day : int, month : int):
    months_sum = day
    months = month - 1
    for i in range(months):
        months_sum += Months[i + 1]
    print("It's the " + str(months_sum) + " day of the year")




dateType =  create_input_var(
    "Insert 1 if you want to convert from month day to whole year day\nInsert 2 if you want to do the opposite ",
    "You can only insert either one or two in numbers\n",
    int
    )


if dateType == 1:
    date = create_input_var(
        "Insert your date with DD/MM format: ",
        "You must insert two numbers separated by a slash!",
        str
    )
    i = 0
    day, month = map(int, date.split("/"))
    convert_from_month(day, month)
elif dateType == 2:
    date = create_input_var(
        "Insert your date in numbers: ",
        "You must insert a number!",
        int
    )
    convert_from_year(date)
else:
    print("Number is out of bounds!")




