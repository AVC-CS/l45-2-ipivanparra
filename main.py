import random


def main():
    total = 0
    numbers = []
    total = 0
    i = 0
    for i in range(5):
        numbers.apped(random.randint(0,100))
        print (numbers[i], end = ' ')
        
      

    print(f'The random values are {numbers}')
    print(f'The total is {total}')

    ########################################
    # Do not delete the return statement
    ########################################
    return numbers, total


if __name__ == '__main__':
    main()
