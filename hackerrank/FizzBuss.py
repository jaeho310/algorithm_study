def fizzBuzz(n):
    for i in range(1,n+1):
        isFizz = False
        isBuzz = False
        if i%3 == 0:
            isFizz = True
        if i%5 == 0:
            isBuzz = True
        if isFizz and isBuzz:
            print('FizzBuzz')
        elif isFizz:
            print('Fizz')
        elif isBuzz:
            print('Buzz')
        else:
            print(i)

if __name__ == '__main__':
    n = int(input().strip())

    fizzBuzz(n)