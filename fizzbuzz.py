def fizzbuzz(number: int):
    x = 1
    while x <= number:
        if x % 3 == 0 and x % 5 == 0:
            print('FizzBuzz')
        elif x % 3 == 0 and x % 5 != 0:
            print('Fizz')
        elif x % 3 != 0 and x % 5 == 0:
            print('Buzz')
        else:
            print(x)
        x += 1
