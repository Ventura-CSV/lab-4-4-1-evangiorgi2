def main():

        number = int(input('Enter a number: '))
        
        while (number < 0 or number > 100):
            number = int(input('The number should be between 0 and 100: '))
        print(number)

        return number


if __name__ == '__main__':
    main()
