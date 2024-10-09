import random


def main():
    total = 0
    numbers = []
    total = 0
    i = 0
    for i in range(5):
        numbers.apped(random.randint(0,100))
        print (numbers[i], end = ' ')
        total += numbers[i]
    print(total, end='')
        
      

    ########################################
    # Do not delete the return statement
    ########################################
    return numbers, total


if __name__ == '__main__':
    main()
