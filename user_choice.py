num1=0
while num1 < 5:
    print("Which Operation do you want to perform:")
    print("\nType 1 for Prime Number")
    print("\nType 2 for Factorial")
    print("\nType 3 for Palindrom")
    print("\nType 4 for Armstrong number")
    print("\nType 5 to ***Exit***")
    uchoice=input("\nWhich Operation do you want to perform:")
    #uchoicestr=str(uchoice)

    match uchoice:
        case '1':
            num = int(input("Enter a number: "))
            if num > 1:
                for i in range(2,num):
                    if (num % i) == 0:
                        print(num,"is not a prime number")         
                        break
                else:
                    print(num,"is a prime number") 
            else:
                print(num,"is not a prime number")

        case '2':
            num = int(input("Enter a number: "))
            factorial = 1
            if num < 0:
                print("Sorry, factorial does not exist for negative numbers")
            elif num == 0:
                print("The factorial of 0 is 1")
            else:
                for i in range(1,num + 1):
                    factorial = factorial*i
                print("The factorial of",num,"is",factorial)

        case '3':
            num = input("Enter a number")
            if num == num[::-1]:
                print(num,"is a palindrome")
            else:
                print(num,"is not a palindrome")

        case '4':
            num = int(input("Enter a number: "))
            sum = 0

            temp = num
            while temp > 0:
                digit = temp % 10
                sum += digit ** 3
                temp //= 10
            if num == sum:
                print(num,"is an Armstrong number")
            else:
                print(num,"is not an Armstrong number")

        case '5':
            exit
    num1 = uchoice
    num1=int(num1)
