def main():
    import random
    print(random.randint(5, 20))  # line 1
    print(random.randrange(3, 10, 2))  # line 2
    print(random.uniform(2.5, 5.5))  # line 3

    print(random.randint(1, 100))


if __name__ == '__main__':
    main()
    """
    What did you see on line 1?
    What was the smallest number you could have seen, what was the largest?
        The smallest number is 5, the largest is 19.
    What did you see on line 2?
    What was the smallest number you could have seen, what was the largest?
        The smallest is 3, the largest is 9
    Could line 2 have produced a 4?
        No, because 3 is odd number when increment by 2 the value will still be odd. 
    What did you see on line 3?
    What was the smallest number you could have seen, what was the largest?
        The smallest is 2.6867561274148835, the largest is 5.465055553549128 
    """
