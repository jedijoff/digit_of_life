date_of_birth = input("Enter your date of birth in DDMMYYYY format: ")
int_date = int(date_of_birth)


def digit_of_life(test_dob):

    sum = 0
    list = []

    for number in str(test_dob):
        sum += int(number)
        list.append(number)

    if len(list) == 1:
        print(f"Your digit of life is: ", list[0])

    else:
        digit_of_life(sum)


digit_of_life(int_date)

