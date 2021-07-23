for fizzbuzz in range(100):
    if fizzbuzz % 15 == 0:
        print('FizzBuzz')
    elif fizzbuzz % 3 == 0:
        print('Fizz')
    elif fizzbuzz % 5 == 0:
        print('Buzz')
    else:
        print(fizzbuzz)