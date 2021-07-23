'''for fizzbuzz in range(1, 100):
    if fizzbuzz % 15 == 0:
        print('FizzBuzz')
    elif fizzbuzz % 3 == 0:
        print('Fizz')
    elif fizzbuzz % 5 == 0:
        print('Buzz')
    else:
        print(fizzbuzz)'''

#alternative approach
c3 = c5 = 0
for fizzbuzz in range(1, 100):
    c3+=1
    c5+=1
    s = ""
    if c3 == 3:
        s += "Fizz"
        c3 = 0
    if c5 == 5:
        s += "Buzz"
        c5 = 0
    
    if s == "":
        print(fizzbuzz)
    else:
        print(s)