def find_fib(n):
    """Fibonacci Sequence - Enter a number
    and have the program generate the Fibonacci
    sequence to that number or to the Nth number."""
    a = 0
    b = 1
    for i in range(n-1):
        a, b = b, a + b
    return b


def main():
    n = int(input()) #input the num of fibbonacci you want to get
    print(find_fib(n))


if __name__ == "__main__":
    main()