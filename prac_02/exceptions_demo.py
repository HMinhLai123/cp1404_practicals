def main():
    """
    CP1404/CP5632 - Practical
    Answer the following questions:
    1. When will a ValueError occur?
        When user enter a non integer values or float values
    2. When will a ZeroDivisionError occur?
        when user enter 0 for the denominator
    3. Could you change the code to avoid the possibility of a ZeroDivisionError?
        yes, just send an error message to user when they enter 0
    """

    try:
        numerator = int(input("Enter the numerator: "))
        denominator = int(input("Enter the denominator: "))
        while denominator == 0:
            print("please enter a positive value (> 0)")
            denominator = int(input("Enter the denominator: "))
        fraction = numerator / denominator
        print(fraction)
    except ValueError:
        print("Numerator and denominator must be valid numbers!")
    except ZeroDivisionError:
        print("Cannot divide by zero!")
    print("Finished.")


if __name__ == '__main__':
    main()
