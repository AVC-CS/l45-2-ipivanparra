import random


def main():
    numbers = []
    total = 0
    i = 0

    for i in range(5):                           
        numbers.append(random.randint(0,100)) 
        print (numbers[i], end= ' ')
        if total > 100:                     # if-else statement to state that if the total is greater than 100 break. 
                break
        else: total += numbers[i]           # else continue adding to the total. 

    print(total)
            
    return numbers, total


if __name__ == '__main__':
    main()
