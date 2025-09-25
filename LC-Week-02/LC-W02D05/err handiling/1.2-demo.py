from one_two_err import ValueTooLargeError, ValueTooSmallError

# you need to guess this number
main_number = 10
result_2 = True
# user guesses a number until he/she gets it right
while result_2:
    try:
        i_num = int(input("Enter a number: "))
        if i_num < main_number:
            raise ValueTooSmallError
        elif i_num > main_number:
            raise ValueTooLargeError
        break
    except ValueTooSmallError:
        print("This value is too small, try again!")
        print("=================")
    except ValueTooLargeError:
        print("This value is too large, try again!")
        print("=================")


print("Congratulations! You guessed it correctly.")
