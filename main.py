import random


def main():
    total = 0
    numbers = []
    total = 0
    i = 0
    for i in range(5):                              # Range of 5 numbers. 
        numbers.append(random.randint(0,100))        # Use the append function to add the numbers you obtain to the list.
        print (numbers[i], end = ' ')               # print numbers with spacing. 
        total += numbers[i]                         # New total is from the previous total plus the new number. 
    print(total, end='')
        

    return numbers, total


if __name__ == '__main__':
    main()
