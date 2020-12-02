def main():
    import random
    out_file = open("results.txt", "w")
    read_file = open("results.txt", "r")
    number = int(input("Enter score: "))
    for i in range(0, number):
        score = random.randint(0, 100)

        if score < 0 or score > 100:
            print("Invalid score")
        else:
            if score > 100:
                print("{} Invalid score".format(score), file=out_file)
            if score >= 90:
                print("{} is Excellent".format(score), file=out_file)
            elif score >= 50:
                print("{} is Passable".format(score), file=out_file)
            else:
                print("{} is Bad".format(score), file=out_file)
    out_file.close()
    #print(read_file.read())

    read_file.close()


if __name__ == '__main__':
    main()
