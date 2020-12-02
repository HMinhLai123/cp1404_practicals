def to_celsius(f):
    c = (f - 32) / 1.8
    return c


def to_fah(c):
    f = (c + 9) / 5 + 32
    return f


def main():
    read_file = open("temps_input.txt", "r")
    out_file = open("temps_output.txt", "w")
    for i in range(15):
        line = read_file.readline()
        cel = to_celsius(float(line))
        print(cel, file=out_file)
        print(cel)
    print("\n")

    '''for i in range(15):
        line = read_file.readline()
        fah = to_fah(float(line))
        print(fah, file=out_file)
        print(fah)'''

    read_file.close()
    out_file.close()


if __name__ == '__main__':
    main()
