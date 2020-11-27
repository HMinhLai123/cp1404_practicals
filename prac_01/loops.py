def main():
    for i in range(1, 21, 2):
        print(i, end=' ')
    print()

    for i in range(0, 110, 10):
        print(i, end=' ')
    print()
    for i in range(20, 0, -1):
        print(i, end=' ')
    print()

    number_of_stars = int(input("Number of stars: "))
    for i in range(0, number_of_stars):
        print(end='*')
    print()

    number_of_stars = int(input("Number of stars: "))
    for i in range(0, number_of_stars):
        for k in range(0, i + 1):
            print('*', end='')
        print("\n")
    print()


if __name__ == '__main__':
    main()
