day = int(input("Enter the number :"))
match day:
    case 1:
        print("monday")
    case 2:
        print("tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("invalid number")
