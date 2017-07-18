"""Have the user enter a number
 and find all Prime Factors (if there are any)
  and display them."""
def if_prime_fact(n):
    #print('checking n=', str(n))
    if n == 2:
        #print('yep')
        return True
    if n % 2 == 0:
        #print('nope, %2')
        return False
    if n > 2:
        for i in range(3,n,2):
            if n % i == 0:
                #print('nope, n>2')
                return False
        #print('yep')
        return True


def calculate_factors(n):
    number = n
    for i in range(2, n+1):
        #print('number of iteration: ',str(i))
        if if_prime_fact(i) and (n % i == 0):
            print('I found a prime factor!: ', str(i))
            number //= i
            #print('currently number is: ', str(number))





def main():
    n = int(input("Enter a number: "))
    calculate_factors(n)


if __name__ == "__main__":
    main()