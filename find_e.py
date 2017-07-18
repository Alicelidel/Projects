""""Find e to the Nth Digit
Enter a number and have the program generate e up to that many decimal places.
Keep a limit to how far the program will go"""


def find_e(n):
    factorial = 1
    e = 1
    for i in range(15):
        e += 1/factorial
        factorial *= (factorial + 1)
        output = str(e)
    return output[:n+2]


def main():
    n = int(input('Enter a number between 1-10'))
    if (n<0)or(n>10):
        print('Too big or too low number number')
        n = 10
    print(find_e(n))


if __name__ == "__main__":
    main()