def main():
    total = 0
    total1 = 0

    out_file = open("name.txt", "w")
    name = input("what is your name?: ")
    print("{}".format(name), file=out_file)
    out_file.close()

    in_file = open("name.txt", "r")
    print("Your name is {}".format(in_file.read()))
    in_file.close()

    read_file = open("numbers.txt", "r")
    # take the first 2 lines and display the total
    for i in range(2):
        first_two_lines = read_file.readline()
        total = total + int(first_two_lines)
    print("The total is {} ".format(total))
    read_file.close()

    # read all lines and print total
    read_file1 = open("numbers.txt", "r")
    for line in read_file1:
        total1 = total1 + int(line)
    print("The total for all lines is {} ".format(total1))
    read_file1.close()


if __name__ == '__main__':
    main()
