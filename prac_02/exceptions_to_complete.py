def main():
    """
    CP1404/CP5632 - Practical
    Fill in the TODOs to complete the task
    """

    finished = False
    result = 0
    while not finished:
        try:
            # TODO: this line
            integer = int(input("please enter an integer: "))
            # TODO: this line
            if type(integer) == int:
                finished = True
        except ValueError:
            print("Please enter a valid integer.")
    print("Valid result is:", result)


if __name__ == '__main__':
    main()
