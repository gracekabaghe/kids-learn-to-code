def rate(list_of_numbers):
    for number in list_of_numbers:
        if number > 50:
            print(number, " is high. ")
        else:
            print(number, " is low.")

rate([2, 20, 60])