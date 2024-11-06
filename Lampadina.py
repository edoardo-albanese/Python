safe_floor = 0
unsafe_floor = 0
current_floor = 0

steps = 1

max_floor = int(input("How many stories high is the building? (Must be a multiple of 5)"))
right_floor = int(input("What is the floor the lamp starts breaking at?"))

def found_lamp():
    print("Found lamp in " + str(steps) + " steps!")

if type(max_floor) != int or max_floor % 5 != 0 or type(right_floor) != int:
    print("Select a multiple of 5 and a whole number!")
else:
    skip_step = int(max_floor / 5)
    print("Divisor: ", skip_step)
    for i in range(round(max_floor / skip_step)):
        if current_floor < right_floor:
            safe_floor = current_floor
            current_floor += skip_step
        elif current_floor == right_floor:
            found_lamp()
            break
        else:
            unsafe_floor = current_floor
            break
        steps += 1
        print("Added step, currently at: ", current_floor)


for floor in range(safe_floor, unsafe_floor):
    if floor == right_floor:
        found_lamp()
        break
    else:
        print("Added step, currently at: ", floor)
    steps += 1